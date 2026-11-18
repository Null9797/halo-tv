const UUID = /^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$/;
const TOKEN = /^[a-f0-9]{64}$/;
const DAY = 86400000;
const ISSUE_URL = 'https://github.com/Null9797/halo-tv/issues/new?template=bug_report.yml';
const headers = {
 'Content-Type':'application/json; charset=utf-8', 'Cache-Control':'no-store',
 'Access-Control-Allow-Origin':'*', 'Access-Control-Allow-Headers':'Content-Type, Authorization',
 'Access-Control-Allow-Methods':'GET, OPTIONS', 'X-Content-Type-Options':'nosniff',
 'Referrer-Policy':'no-referrer'
};
const json = (data, status = 200) => new Response(JSON.stringify(data), {status, headers});
const hash = async text => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text))), x=>x.toString(16).padStart(2,'0')).join('');
const bearer = req => (req.headers.get('Authorization') || '').replace(/^Bearer /, '');

export async function handle(request, env) {
 const path = new URL(request.url).pathname.replace(/^\/api\/feedback\/?/,'').split('/').filter(Boolean);
 if (request.method === 'OPTIONS') return new Response(null,{status:204,headers});
 if (path[0] !== 'admin') return json({error:'feedback_moved', url:ISSUE_URL},410);
 if (request.method !== 'GET') return json({error:'read_only'},405);
 try {
  if(!env.FEEDBACK_DB || !TOKEN.test(env.FEEDBACK_ADMIN_HASH || ''))return json({error:'service_not_ready'},503);
  const db=env.FEEDBACK_DB, cutoff=Date.now()-30*DAY;
  const key=bearer(request);
  if(!TOKEN.test(key) || await hash(key)!==env.FEEDBACK_ADMIN_HASH)return json({error:'unauthorized'},401);
  if(path.length===1) {
   const u=new URL(request.url), status=u.searchParams.get('status') || '', edition=u.searchParams.get('edition') || '', version=(u.searchParams.get('version')||'').slice(0,40), model=(u.searchParams.get('model')||'').slice(0,160);
   const rows=await db.prepare('SELECT id,created,category,edition,version,model,status FROM reports WHERE created>=? AND (?=\'\' OR status=?) AND (?=\'\' OR edition=?) AND (?=\'\' OR version=?) AND (?=\'\' OR instr(model,?)>0) ORDER BY created DESC LIMIT 400').bind(cutoff,status,status,edition,edition,version,version,model,model).all();
   return json({items:rows.results});
  }
  if(path.length!==2 || !UUID.test(path[1]))return json({error:'not_found'},404);
  const item=await db.prepare('SELECT id,created,updated,category,edition,version,code,model,android,diagnostics,description,status,reply,images FROM reports WHERE id=? AND created>=?').bind(path[1],cutoff).first();
  return item?json(item):json({error:'not_found'},404);
 } catch { return json({error:'temporarily_unavailable'},503); }
}

export default { async fetch(request, env) {
 const path = new URL(request.url).pathname;
 if (path === '/api/feedback' || path.startsWith('/api/feedback/')) return handle(request, env);
 return env.ASSETS.fetch(request);
}};
