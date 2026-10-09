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
const opts = {display: true, em: 16, ex: 8, containerWidth: 1280};

const a = doc.convert('\\chi_p(y)^3 + x', Object.assign({}, opts, {display: false}));
const b = doc.convert('\\begin{cases} 1, & x > 0, \\\\ 0, & \\text{其他情形}. \\end{cases}', opts);
console.log('--- inline container html ---');
console.log(adaptor.outerHTML(a).slice(0, 900));
console.log('\n--- CJK cases svg ---');
console.log(adaptor.outerHTML(b).slice(0, 1500));
const whole = adaptor.outerHTML(doc.document);
const i = whole.indexOf('MJX-SVG-global-cache');
console.log('\nglobal cache present:', i >= 0, '| doc len:', whole.length);
console.log('context:', whole.slice(Math.max(0, i - 80), i + 200).replace(/\n/g, ' '));
console.log('first svg has <defs>:', adaptor.outerHTML(a).includes('<defs>'));
console.log('cjk svg has <text>:', adaptor.outerHTML(b).includes('<text'));
const m = adaptor.outerHTML(b).match(/<text[^>]*>[\s\S]{0,200}/);
console.log('text node sample:', m ? m[0].replace(/\n/g, ' ') : '(none)');
