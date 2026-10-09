// tex2svg.js — batch LaTeX -> SVG via MathJax v3 (offline, no browser needed)
// usage: node tex2svg.js input.json output.json
//   input : [{"key": "...", "latex": "...", "display": true|false}, ...]
//   output: {"<key>": {"svg": "..."} | {"error": "..."}}
const fs = require('fs');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const tex = new TeX({
  packages: AllPackages,
  formatError: (jax, err) => { throw err; },
});
const svg = new SVG({fontCache: 'local'});
const doc = mathjax.document('', {InputJax: tex, OutputJax: svg});

const inp = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = {};
let ok = 0, bad = 0;

for (const item of inp) {
  try {
    const node = doc.convert(item.latex, {
      display: !!item.display, em: 16, ex: 8, containerWidth: 80 * 16,
    });
    let s = adaptor.outerHTML(node);
    const m = s.match(/<svg[\s\S]*<\/svg>/);
    if (!m) throw new Error('no <svg> in output');
    s = m[0].replace(/MJX-(\d+)-/g, 'MJX-' + item.key + '-');
    out[item.key] = {svg: s};
    ok++;
  } catch (e) {
    out[item.key] = {error: String((e && e.message) || e).slice(0, 200)};
    bad++;
  }
}
fs.writeFileSync(process.argv[3], JSON.stringify(out));
console.error('tex2svg: ok=' + ok + ' error=' + bad);
