/* Collision check for the composition's base furniture vs. its clip cards.
   The bottom-left slug line once sat under the card's corner; this makes that
   class of bug fail loudly instead of shipping. Run before every render.
     node src/check_layout.js src/index.html                                  */
const {chromium}=require('playwright'); const path=require('path');
const FURNITURE=['#chNum','#chName','#slug','#yr'];
const hit=(a,b)=>!(a.r<=b.x||b.r<=a.x||a.b<=b.y||b.b<=a.y);
(async()=>{
  const file=path.resolve(process.argv[2]||'src/index.html');
  const br=await chromium.launch({args:['--no-sandbox']});
  const p=await br.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+file); await p.waitForTimeout(800);
  const {furn,shots}=await p.evaluate(sels=>{
    const box=e=>{const r=e.getBoundingClientRect();
      return {x:Math.round(r.x),y:Math.round(r.y),r:Math.round(r.right),b:Math.round(r.bottom)};};
    // furniture is hidden at t=0, so measure it forced-visible
    const furn=sels.map(s=>{const e=document.querySelector(s); if(!e) return null;
      const o=e.style.opacity; e.style.opacity=1;
      if(!e.textContent.trim()) e.textContent='SAMPLE SLUG LINE\nPrelinger Archives · public domain';
      const b=box(e); b.n=s; e.style.opacity=o; return b;}).filter(Boolean);
    const shots=[...document.querySelectorAll('.shot')].map(e=>{const b=box(e);
      b.n=e.id; b.full=e.classList.contains('full'); return b;});
    return {furn,shots};
  }, FURNITURE);
  let fails=0;
  for(const f of furn) for(const s of shots){
    if(s.full) continue;                        // full-bleed sits under the furniture by design
    if(hit(f,s)){fails++; console.log(`COLLIDE ${f.n} [y${f.y}-${f.b}] x .shot#${s.n} [y${s.y}-${s.b}]`);}
  }
  const stageBottom=Math.max(...shots.filter(s=>!s.full).map(s=>s.b));
  const slug=furn.find(f=>f.n==='#slug');
  console.log(`cards=${shots.length}  lowest card bottom=${stageBottom}  slug top=${slug.y}  gap=${slug.y-stageBottom}px`);
  if(slug.y-stageBottom<16){fails++; console.log('TOO TIGHT: need >=16px between the lowest card and the slug');}
  console.log(fails?`\nFAIL — ${fails} issue(s)`:'\nPASS — no furniture/footage collisions');
  await br.close(); process.exit(fails?1:0);
})();
