const TYPES = new Set(['guard', 'performance', 'wallpaper', 'update', 'weather', 'phone', 'other']);
const EDITIONS = new Set(['standard', 'guard', 'lite']);
const UUID = /^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$/;
const TOKEN = /^[a-f0-9]{64}$/;
const DAY = 86400000;
export const headers = {
 'Content-Type':'application/json; charset=utf-8', 'Cache-Control':'no-store',
 'Access-Control-Allow-Origin':'*', 'Access-Control-Allow-Headers':'Content-Type, Authorization',
 'Access-Control-Allow-Methods':'GET, POST, OPTIONS', 'X-Content-Type-Options':'nosniff',
 'Referrer-Policy':'no-referrer'
};
const json = (data, status = 200) => new Response(JSON.stringify(data), {status, headers});
const hash = async text => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text))), x=>x.toString(16).padStart(2,'0')).join('');
const bearer = req => (req.headers.get('Authorization') || '').replace(/^Bearer /, '');
export function redact(value) {
 return String(value || '').slice(0, 100000)
 .replace(/https?:\/\/[^\s<>"']+/gi, '<url>')
 .replace(/(?:\/storage\/|\/sdcard\/|\/data\/user\/)[^\s]+/gi, '<private-path>')
 .replace(/\b(?:\d{1,3}\.){3}\d{1,3}\b/g, '<ip>')
 .replace(/\b(?:[a-f0-9]{2}:){5}[a-f0-9]{2}\b/gi, '<mac>')
 .replace(/(?:[0-9a-f]{0,4}:){2,}[0-9a-f]{0,4}(?:%[a-z0-9]+)?/gi, '<ip>')
 .replace(/[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}/gi, '<email>')
 .replace(/(password|passwd|token|authorization|pin|ssid)\s*[=:]\s*[^\s,;]+/gi,'$1=<redacted>').slice(0,80000);
}
async function body(req, max = 600000) {
 if (!req.headers.get('Content-Type')?.startsWith('application/json')) throw {status:415};
 if (Number(req.headers.get('Content-Length')) > max) throw {status:413};
 const reader = req.body?.getReader(); if (!reader) throw {status:400};
 let size=0, parts=[];
 try { while(true) { const r=await reader.read(); if(r.done)break; size+=r.value.length; if(size>max)throw {status:413}; parts.push(r.value); } }
 finally { await reader.cancel().catch(()=>{}); }
 const data=new Uint8Array(size);let offset=0;for(const p of parts){data.set(p,offset);offset+=p.length;}
 try{return JSON.parse(new TextDecoder('utf-8',{fatal:true}).decode(data));}catch{throw {status:400};}
}
function bounded(v, length) { if (typeof v !== 'string' || v.length>length) throw {status:400};return v; }
function images(value) {
 if (!Array.isArray(value) || value.length>2) throw {status:400};
 return value.map(s=> {
  if (typeof s !== 'string' || s.length>250000 || !/^data:image\/(jpeg|png);base64,[A-Za-z0-9+/]+=*$/.test(s)) throw {status:400};
  let b;try{b=atob(s.split(',')[1]);}catch{throw {status:400};}
  if(b.length>180000 || !(s.startsWith('data:image/jpeg;') && b.startsWith('\xff\xd8\xff') || s.startsWith('data:image/png;') && b.startsWith('\x89PNG\r\n\x1a\n'))) throw {status:400};
  return s;
 });
}
export async function handle(request, env) {
 try {
  if(request.method==='OPTIONS')return new Response(null,{status:204,headers});
  const path=new URL(request.url).pathname.replace(/^\/api\/feedback\/?/,'').split('/').filter(Boolean);
  if(!env.FEEDBACK_DB || !TOKEN.test(env.FEEDBACK_ADMIN_HASH || ''))return json({error:'service_not_ready'},503);
  const db=env.FEEDBACK_DB, now=Date.now(), cutoff=now-30*DAY;
  if(path[0]==='admin') {
   const key=bearer(request);
   if(!TOKEN.test(key) || await hash(key)!==env.FEEDBACK_ADMIN_HASH)return json({error:'unauthorized'},401);
   if(request.method==='GET' && path.length===1) {
    const u=new URL(request.url), status=u.searchParams.get('status') || '', edition=u.searchParams.get('edition') || '', version=(u.searchParams.get('version')||'').slice(0,40), model=(u.searchParams.get('model')||'').slice(0,160);
    const rows=await db.prepare('SELECT id,created,category,edition,version,model,status FROM reports WHERE created>=? AND (?=\'\' OR status=?) AND (?=\'\' OR edition=?) AND (?=\'\' OR version=?) AND (?=\'\' OR instr(model,?)>0) ORDER BY created DESC LIMIT 400').bind(cutoff,status,status,edition,edition,version,version,model,model).all();
    return json({items:rows.results});
   }
   if(path.length!==2 || !UUID.test(path[1]))return json({error:'not_found'},404);
   if(request.method==='GET') {
    const item=await db.prepare('SELECT id,created,updated,category,edition,version,code,model,android,diagnostics,description,status,reply,images FROM reports WHERE id=? AND created>=?').bind(path[1],cutoff).first();
    return item?json(item):json({error:'not_found'},404);
   }
   if(request.method==='POST') {
    const b=await body(request,16000);if(!['new','working','resolved'].includes(b.status))throw {status:400};
    const reply=bounded(b.reply,3000);
    const result=await db.prepare('UPDATE reports SET status=?,reply=?,updated=? WHERE id=? AND created>=?').bind(b.status,reply,now,path[1],cutoff).run();
    return result.meta.changes ? json({saved:true}) : json({error:'not_found'},404);
   }
   return json({error:'method'},405);
  }
  if(path.length===0 && request.method==='POST') {
   const b=await body(request,300000);
   if(b.schema!==1 || b.consent!==true || !UUID.test(b.id) || !TOKEN.test(b.token) || !TYPES.has(b.category) || !EDITIONS.has(b.edition) || !Number.isSafeInteger(b.code) || b.code<1)throw {status:400};
   const proof=await hash(b.token);
   const previous=await db.prepare('SELECT proof,status,created FROM reports WHERE id=?').bind(b.id).first();
   if(previous) return previous.proof===proof && previous.created>=cutoff ? json({saved:true,id:b.id,status:previous.status}) : json({error:'conflict'},409);
   const version=bounded(b.version,40),model=bounded(b.model,160),android=bounded(b.android,80),diagnostics=redact(bounded(b.diagnostics,80000));
   // Delete only expired reports; never collect device IDs or retain source IP addresses.
   await db.prepare('DELETE FROM reports WHERE created<?').bind(cutoff).run();
   const rate=await hash(env.FEEDBACK_ADMIN_HASH+Math.floor(now/DAY)+(request.headers.get('CF-Connecting-IP')||'unknown'));
   const r=await db.prepare(`INSERT OR IGNORE INTO reports (id,proof,created,updated,category,edition,version,code,model,android,diagnostics,rate_key)
    SELECT ?,?,?,?,?,?,?,?,?,?,?,? WHERE (SELECT count(*) FROM reports)<400 AND (SELECT count(*) FROM reports WHERE created>=?)<100 AND (SELECT count(*) FROM reports WHERE rate_key=? AND created>=?)<10`)
    .bind(b.id,proof,now,now,b.category,b.edition,version,b.code,model,android,diagnostics,rate,now-DAY,rate,now-DAY).run();
   if(!r.meta.changes) {
    const retry=await db.prepare('SELECT proof,status FROM reports WHERE id=?').bind(b.id).first();
    if(retry?.proof===proof)return json({saved:true,id:b.id,status:retry.status});
    return json({error:'limit_reached',retryable:true},429);
   }
   return json({saved:true,id:b.id,status:'new'},201);
  }
  if(path.length===1 && UUID.test(path[0])) {
   const key=bearer(request);if(!TOKEN.test(key))return json({error:'not_found'},404);
   const proof=await hash(key);
   const row=await db.prepare('SELECT status,reply,description,images,created FROM reports WHERE id=? AND proof=? AND created>=?').bind(path[0],proof,cutoff).first();
   if(!row)return json({error:'not_found'},404);
   if(request.method==='GET' && new URL(request.url).searchParams.get('summary')==='1')return json({id:path[0],status:row.status,reply:row.reply,created:row.created});
   if(request.method==='GET')return json({id:path[0],status:row.status,reply:row.reply,description:row.description,created:row.created,images:JSON.parse(row.images)});
   if(request.method==='POST') {
    const b=await body(request);if(b.consent!==true)throw {status:400};
    const description=bounded(b.description,3000),media=images(b.images || []);
    await db.prepare('UPDATE reports SET description=?,images=?,updated=? WHERE id=? AND proof=? AND created>=?').bind(description,JSON.stringify(media),now,path[0],proof,cutoff).run();
    return json({saved:true,id:path[0]});
   }
  }
  return json({error:'not_found'},404);
 } catch (err) { return json({error:err?.status ? 'invalid_request' : 'temporarily_unavailable'},err?.status || 503); }
}

export default { async fetch(request, env) {
 const path = new URL(request.url).pathname;
 if (path === '/api/feedback' || path.startsWith('/api/feedback/')) return handle(request, env);
 return env.ASSETS.fetch(request);
}};
