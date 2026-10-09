const fs = require('fs');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({packages: AllPackages, formatError: (jax, err) => { throw err; }});

function run(mode) {
  const svg = new SVG({fontCache: mode});
  const doc = mathjax.document('', {InputJax: tex, OutputJax: svg});
  const tests = {
    inline: [false, '\\chi_p(y)^3'],
    display: [true, 'G(vw) = G(v)G(w)R(v, w), \\quad G(1) = 1. \\tag{4.5}'],
    dblbackslash: [true, 'a = b, \\\\ c = d.'],
    matrix: [true, '\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}'],
    cases: [true, '\\begin{cases} 1, & x > 0, \\\\ 0, & x \\le 0. \\end{cases}'],
    cjk: [true, '\\text{其他情形} + x^2'],
  };
  const res = {};
  for (const [k, [disp, latex]] of Object.entries(tests)) {
    try {
      const node = doc.convert(latex, {display: disp, em: 16, ex: 8, containerWidth: 80 * 16});
      const s = adaptor.outerHTML(node);
      const m = s.match(/<svg[\s\S]*<\/svg>/);
      res[k] = m ? m[0].length + ' bytes | ' + m[0].slice(0, 70) : 'NO SVG';
    } catch (e) { res[k] = 'ERROR ' + String(e.message || e).slice(0, 120); }
  }
  let sheet = '';
  try {
    const sh = svg.styleSheet(doc);
    sheet = sh ? adaptor.outerHTML(sh) : '(none)';
  } catch (e) { sheet = 'ERROR ' + e.message; }
  console.log('=== fontCache=' + mode + ' ===');
  for (const [k, v] of Object.entries(res)) console.log('  ' + k.padEnd(14), v);
  console.log('  styleSheet len:', sheet.length, '|', sheet.slice(0, 90).replace(/\n/g, ' '));
}
run('local');
run('global');
