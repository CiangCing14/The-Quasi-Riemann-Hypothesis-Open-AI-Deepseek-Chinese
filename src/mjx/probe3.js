const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({packages: AllPackages, formatError: (jax, err) => { throw err; }});
const svg = new SVG({fontCache: 'global'});
const doc = mathjax.document('', {InputJax: tex, OutputJax: svg});
const opts = {em: 16, ex: 8, containerWidth: 1280};

const a = adaptor.outerHTML(doc.convert('\\chi_p(y)^3 + x', Object.assign({}, opts, {display: false})));
const b = adaptor.outerHTML(doc.convert('\\begin{cases} 1, & x > 0, \\\\ 0, & \\text{其他情形}. \\end{cases}', Object.assign({}, opts, {display: true})));
const c = adaptor.outerHTML(doc.convert('\\alpha + \\beta', Object.assign({}, opts, {display: false})));

console.log('first svg has <defs>:', a.includes('<defs>'));
console.log('second svg has <defs>:', b.includes('<defs>'));
console.log('third svg has <defs>:', c.includes('<defs>'));
console.log('third svg len:', c.length);
console.log('a len:', a.length, 'b len:', b.length);
console.log('CJK chars present in b:', /[\u4e00-\u9fff]/.test(b), '| sample:', (b.match(/[\u4e00-\u9fff]+/g) || []).join(','));
const m = b.match(/<text[^>]*>[\s\S]{0,160}/);
console.log('text node in b:', m ? m[0].replace(/\s+/g, ' ') : '(none)');
const whole = adaptor.outerHTML(doc);
console.log('doc type:', typeof whole, '| len:', whole && whole.length);
console.log('defs occurrences in whole doc:', (whole.match(/<defs>/g) || []).length);
console.log('svgs in whole doc:', (whole.match(/<svg/g) || []).length);
console.log('has MJX-SVG-global-cache:', whole.includes('MJX-SVG-global-cache'));
