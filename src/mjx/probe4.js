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

doc.convert('\\chi_p(y)^3 + \\alpha', Object.assign({}, opts, {display: false}));
doc.convert('\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}', Object.assign({}, opts, {display: true}));

const body = adaptor.outerHTML(adaptor.body(doc));
console.log('body len:', body.length);
console.log('global cache in body:', body.includes('MJX-SVG-global-cache'));
console.log('defs count in body:', (body.match(/<defs>/g) || []).length);
const i = body.indexOf('MJX-SVG-global-cache');
console.log('cache context:', i >= 0 ? body.slice(Math.max(0, i - 100), i + 300).replace(/\s+/g, ' ') : '(absent)');
console.log('body head:', body.slice(0, 300).replace(/\s+/g, ' '));
// how big is the defs payload?
const d = body.indexOf('<defs>');
if (d >= 0) console.log('defs payload len:', body.length - d);
