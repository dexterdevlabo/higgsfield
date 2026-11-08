/* Dense pre-render QC: samples the timeline every N seconds, parks each video at
   its own in-point, and reports per-frame mean luma + bright extreme.
   blackdetect is the wrong instrument for this palette (see films/shortwhy). */
const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path');
const STEP=+(process.argv[3]||4), OUT=process.argv[4]||'/tmp/qc';
(async()=>{
  fs.mkdirSync(OUT,{recursive:true});
  const br=await chromium.launch({args:['--no-sandbox']});
  const p=await br.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
  await p.goto('file://'+path.resolve(process.argv[2])); await p.waitForTimeout(3000);
  const dur=await p.evaluate(()=>window.__timelines.root.duration());
  await p.evaluate(()=>document.querySelectorAll('video').forEach(v=>v.pause()));
  const rows=[];
  for(let t=0;t<=dur;t+=STEP){
    await p.evaluate(async t=>{
      window.__timelines.root.pause(t);
      document.querySelectorAll('.shot video').forEach(v=>{
        const st=+v.dataset.start, du=+v.dataset.duration;
        if(t>=st&&t<=st+du){try{v.currentTime=Math.min((v.duration||du)-0.05,t-st);}catch(e){}}
      });
    }, t);
    await p.waitForTimeout(500);
    const f=`${OUT}/t${String(Math.round(t)).padStart(4,'0')}.png`;
    await p.screenshot({path:f});
    rows.push([t,f]);
  }
  console.log(`sampled ${rows.length} frames over ${dur.toFixed(3)}s`);
  fs.writeFileSync(`${OUT}/frames.txt`, rows.map(r=>r.join(' ')).join('\n'));
  await br.close();
})();
