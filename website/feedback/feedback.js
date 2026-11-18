(() => {
'use strict';
const root=document.querySelector('#app'), API='/api/feedback/admin';
const labels={
 admin:['历史反馈（只读）','Feedback archive (read-only)'],key:['管理员密钥','Administrator key'],
 login:['登录','Sign in'],refresh:['刷新','Refresh'],logout:['退出','Sign out'],back:['返回','Back'],
 loading:['正在处理…','Working…'],all:['全部','All'],new:['待处理','New'],working:['处理中','In progress'],
 resolved:['已处理','Resolved'],unavailable:['暂时无法读取历史反馈','Could not load past feedback'],
 version:['版本','Version'],model:['型号','Model'],count:['记录数','Reports'],filter:['筛选','Filter'],
 guard:['桌面守护','Home guard'],performance:['卡顿 / 黑屏 / 闪退','Stutter / black screen / crash'],
 wallpaper:['壁纸与屏保','Wallpaper & screensaver'],update:['下载与安装更新','Update download & install'],
 weather:['天气异常','Weather'],phone:['手机互联','Phone connection'],other:['其他问题','Other']
};
const language=(navigator.language||'en').startsWith('zh')?0:1;
const t=key=>labels[key]?.[language]||key;
document.querySelector('#tagline').textContent=t('admin');
const el=(tag,text,cls)=>{const e=document.createElement(tag);if(text)e.textContent=text;if(cls)e.className=cls;return e;};
const btn=(text,action,cls='')=>{const b=el('button',text,cls);b.type='button';b.onclick=action;return b;};
const page=(title)=>{root.replaceChildren(el('h1',title));const c=el('section',null,'card');root.append(c);return c;};
let busy=false,adminKey='';
async function request(path='') {
 const ctrl=new AbortController();
 const timer=setTimeout(()=>ctrl.abort(),35000);
 try {
  const response=await fetch(API+path,{headers:{Authorization:'Bearer '+adminKey},signal:ctrl.signal,cache:'no-store'});
  if (!response.ok) throw Error(String(response.status));
  return await response.json();
 } finally {clearTimeout(timer);}
}
async function run(b,fn,msg,fallback='unavailable'){if(busy)return;busy=true;const old=b.textContent;b.disabled=true;b.textContent=t('loading');try{await fn();}catch{if(msg)msg.textContent=t(fallback);}finally{busy=false;b.disabled=false;b.textContent=old;}}
function login(){adminKey='';const c=page(t('admin'));const input=el('input');input.type='password';input.autocomplete='off';input.placeholder=t('key');c.append(input);const msg=el('p',null,'error');const b=btn(t('login'),()=>run(b,async()=>{adminKey=input.value.trim();await request();input.value='';await adminList();},msg));c.append(b,msg);}
async function adminList(){const c=page(t('admin'));const status=el('select');for(const k of ['','new','working','resolved']){const o=el('option',t(k||'all'));o.value=k;status.append(o);}const edition=el('select');for(const k of ['','standard','guard','lite']){const o=el('option',k||t('all'));o.value=k;edition.append(o);}const version=el('input');version.placeholder=t('version');const model=el('input');model.placeholder=t('model');const results=el('div'),msg=el('p',null,'error');async function load(){const q=new URLSearchParams({status:status.value,edition:edition.value,version:version.value,model:model.value});const data=await request('?'+q);results.replaceChildren(el('p',data.items.length+' '+t('count')));for(const r of data.items)results.append(btn(t(r.category)+' · '+r.model+' · '+r.version+' '+r.edition+' · '+t(r.status),()=>adminDetail(r.id),'item'));}const b=btn(t('filter'),()=>run(b,load,msg));c.append(status,edition,version,model,b,btn(t('logout'),login,'secondary'),msg,results);try{await load();}catch{msg.textContent=t('unavailable');}}
async function adminDetail(id) {
 const c=page(t('admin')), msg=el('p',null,'error');
 c.append(msg);
 try {
  const d=await request('/'+id);
  c.append(el('h2',t(d.category)),el('p',d.model+' · '+d.android+' · '+d.version+' / '+d.edition),
    el('p',d.id,'receipt'),el('span',t(d.status),'status'));
  if (d.description) c.append(el('p',d.description));
  if (d.reply) c.append(el('p',d.reply,'muted'));
  c.append(el('pre',d.diagnostics || '—'));
  if (d.images.length) {
   const thumbnails=el('div',null,'thumbs');
   for (const source of JSON.parse(d.images)) {
    const img=el('img');
    img.src=source;
    thumbnails.append(img);
   }
   c.append(thumbnails);
  }
 } catch {msg.textContent=t('unavailable');}
 c.append(btn(t('back'),adminList,'secondary'));
}
login();
})();
