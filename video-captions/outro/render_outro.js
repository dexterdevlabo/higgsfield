// Render outro.html frame-by-frame to PNGs, then encode with ffmpeg.
// usage: node render_outro.js <assets_dir_with_html_avatar_lastframe> <handle> <out.mp4>
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs'), path = require('path');

(async () => {
  const [dir, handle, out] = process.argv.slice(2);
  const FPS = 24, DUR = 4.8;
  const frames = path.join(dir, 'frames');
  fs.rmSync(frames, { recursive: true, force: true }); fs.mkdirSync(frames);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(dir, 'outro.html') + '?h=' + encodeURIComponent(handle));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  for (let i = 0; i < Math.round(FPS * DUR); i++) {
    const t = i * 1000 / FPS;
    await page.evaluate(t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; }), t);
    await page.screenshot({ path: path.join(frames, `f${String(i).padStart(4, '0')}.png`) });
  }
  await browser.close();
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', String(FPS), '-i', path.join(frames, 'f%04d.png'),
    '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', out]);
  console.log('wrote', out);
})();
