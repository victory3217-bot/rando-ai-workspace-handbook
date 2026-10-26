"""Render lecture-slide SVGs with headless Chrome and check them for layout problems.

Usage:  python -I tools/slide_check.py <svg> [<svg> ...] [--png-dir DIR]
For every SVG it writes <png-dir>/<name>.png (1600x900 screenshot, default: a temp folder) and prints
problems found by measuring the real rendered text:
  - text outside the 1600x900 slide (24 px margin)
  - two text lines whose boxes overlap
  - a text line that crosses the edge of a <rect> that contains its centre (text wider than its box)
  - body text smaller than 20 px, and slides that carry too much text
This checks layout only. It does not check whether the content is right.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = next((p for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                           r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe") if os.path.exists(p)), None)

JS = r"""
const svg = document.querySelector('svg');
const vb = svg.viewBox.baseVal;
const issues = [];
const texts = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim());
const boxes = [...svg.querySelectorAll('rect')].map(r => ({el: r, b: r.getBBox()})).filter(x => x.b.width > 0 && x.b.height > 0);
const tb = texts.map(t => {
  const b = t.getBBox();
  // getBBox is in the text's own coordinate system; apply the transform chain to the slide space
  const m = t.getCTM(), s = svg.getCTM();
  const inv = s.inverse().multiply(m);
  const pts = [[b.x, b.y], [b.x + b.width, b.y], [b.x, b.y + b.height], [b.x + b.width, b.y + b.height]].map(([x, y]) => [inv.a * x + inv.c * y + inv.e, inv.b * x + inv.d * y + inv.f]);
  const xs = pts.map(p => p[0]), ys = pts.map(p => p[1]);
  return {t, x0: Math.min(...xs), x1: Math.max(...xs), y0: Math.min(...ys), y1: Math.max(...ys), str: t.textContent.trim().replace(/\s+/g, ' ').slice(0, 40), fs: parseFloat(getComputedStyle(t).fontSize) * (inv.a || 1)};
});
const W = vb.width, H = vb.height, M = 24;
let chars = 0;
tb.forEach(o => {
  chars += o.str.length;
  if (o.x0 < M - 1 || o.x1 > W - M + 1 || o.y0 < M - 1 || o.y1 > H - 8) issues.push('OUT: "' + o.str + '" [' + [o.x0, o.y0, o.x1, o.y1].map(Math.round) + ']');
  if (o.fs < 20) issues.push('SMALL(' + o.fs.toFixed(1) + '): "' + o.str + '"');
});
for (let i = 0; i < tb.length; i++) for (let j = i + 1; j < tb.length; j++) {
  const a = tb[i], b = tb[j];
  const ox = Math.min(a.x1, b.x1) - Math.max(a.x0, b.x0), oy = Math.min(a.y1, b.y1) - Math.max(a.y0, b.y0);
  if (ox > 3 && oy > 5) issues.push('OVERLAP: "' + a.str + '" x "' + b.str + '"');
}
tb.forEach(o => {
  const cx = (o.x0 + o.x1) / 2, cy = (o.y0 + o.y1) / 2;
  // smallest rect containing the text centre
  let best = null;
  boxes.forEach(({el, b}) => {
    const m = el.getCTM(), s = svg.getCTM(), inv = s.inverse().multiply(m);
    const x0 = inv.a * b.x + inv.e, y0 = inv.d * b.y + inv.f, x1 = x0 + b.width * inv.a, y1 = y0 + b.height * inv.d;
    if (cy > y0 && cy < y1 && [cx, o.x0 + 3, o.x1 - 3].some(px => px > x0 && px < x1) && (x1 - x0) < W - 10) {
      if (!best || (x1 - x0) * (y1 - y0) < (best.x1 - best.x0) * (best.y1 - best.y0)) best = {x0, y0, x1, y1};
    }
  });
  if (best && (o.x0 < best.x0 + 2 || o.x1 > best.x1 - 2 || o.y0 < best.y0 + 1 || o.y1 > best.y1 - 1)) {
    issues.push('CROSSES BOX: "' + o.str + '" text [' + [o.x0, o.x1].map(Math.round) + '] box [' + [best.x0, best.x1].map(Math.round) + '] y text [' + [o.y0, o.y1].map(Math.round) + '] box [' + [best.y0, best.y1].map(Math.round) + ']');
  }
});
if (chars > 1100) issues.push('DENSE: ' + chars + ' characters of text (split the slide or cut text)');
document.getElementById('out').textContent = JSON.stringify({chars, texts: tb.length, minFont: Math.min(...tb.map(o => o.fs)), issues});
"""


def run(svg: Path, png_dir: Path):
    src = svg.read_text(encoding="utf-8")
    src = re.sub(r"^<\?xml[^>]*\?>", "", src.strip())
    html = ("<!doctype html><meta charset=utf-8><style>html,body{margin:0;background:#fff}svg{display:block;width:1600px;height:900px}</style>"
            + src + "<pre id=out></pre><script>window.addEventListener('load',()=>{" + JS + "});</script>")
    tmp = Path(tempfile.mkdtemp()) / (svg.stem + ".html")
    tmp.write_text(html, encoding="utf-8")
    base = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1600,900", "--no-first-run"]
    out = subprocess.run(base + ["--virtual-time-budget=2000", "--dump-dom", tmp.as_uri()], capture_output=True, text=True, encoding="utf-8", timeout=90).stdout
    m = re.search(r'<pre id="out">(.*?)</pre>', out, re.S)
    result = json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")) if m and m.group(1).strip() else {"issues": ["could not measure (invalid SVG?)"]}
    png = png_dir / (svg.parent.name + "_" + svg.stem + ".png")
    subprocess.run(base + ["--screenshot=" + str(png), svg.resolve().as_uri()], capture_output=True, timeout=90)
    return result, png


def main(argv):
    png_dir = Path(tempfile.gettempdir()) / "slide-png"
    args = []
    it = iter(argv)
    for a in it:
        if a == "--png-dir":
            png_dir = Path(next(it))
        else:
            args.append(a)
    png_dir.mkdir(parents=True, exist_ok=True)
    bad = 0
    for a in args:
        res, png = run(Path(a), png_dir)
        issues = res.get("issues", [])
        print(f"{a}: texts={res.get('texts')} chars={res.get('chars')} minFont={res.get('minFont') and round(res['minFont'], 1)} png={png}")
        for i in issues:
            print("   ", i)
        bad += bool(issues)
    print("SLIDES WITH PROBLEMS:", bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
