"use strict";(globalThis.webpackChunk=globalThis.webpackChunk||[]).push([["app_assets_modules_github_sticky-scroll-into-view_ts"],{70763(a,b,c){c.d(b,{O4:()=>m,jo:()=>l,Qp:()=>k});var d=c(81574),e=c(59753);let f="ontransitionend"in window;function g(a){return"height"===getComputedStyle(a).transitionProperty}function h(a,b){a.style.transition="none",b(),a.offsetHeight,a.style.transition=""}var i=c(96776);function j(a,b){var c;for(let d of(a.classList.toggle("open",b),a.classList.toggle("Details--on",b),[...(c=a).querySelectorAll(".js-details-target")].filter(a=>a.closest(".js-details-container")===c)))d.setAttribute("aria-expanded",b.toString())}function k(a,b){let c=a.getAttribute("data-details-container")||".js-details-container",d=a.closest(c),e=b?.force?? !d.classList.contains("open"),k=b?.withGroup?? !1;!function(a,b){if(!f){b();return}let c=Array.from(a.querySelectorAll(".js-transitionable"));for(let d of(a.classList.contains("js-transitionable")&&c.push(a),c)){let e=g(d);d instanceof HTMLElement&&(d.addEventListener("transitionend",()=>{d.style.display="",d.style.visibility="",e&&h(d,function(){d.style.height=""})},{once:!0}),d.style.boxSizing="content-box",d.style.display="block",d.style.visibility="visible",e&&h(d,function(){d.style.height=getComputedStyle(d).height}),d.offsetHeight)}for(let i of(b(),c))if(i instanceof HTMLElement&&g(i)){let j=getComputedStyle(i).height;i.style.boxSizing="","0px"===j?i.style.height=`${i.scrollHeight}px`:i.style.height="0px"}}(d,()=>{j(d,e);let b=k?function(a,b){let c=a.getAttribute("data-details-container-group");return c?((0,i.uQ)(a,()=>{var d;for(let e of(d=c,[...document.querySelectorAll(".js-details-container")].filter(a=>a.getAttribute("data-details-container-group")===d)))e!==a&&j(e,b)}),c):null}(d,e):null;Promise.resolve().then(()=>{var c,f;(function(a,b){b.find(b=>{let c=a.querySelectorAll(b),d=c[c.length-1];if(d&&document.activeElement!==d)return d.focus(),!0})})(c=d,[".js-focus-on-dismiss","input[autofocus], textarea[autofocus]"]),(f=a).classList.contains("tooltipped")&&(f.classList.remove("tooltipped"),f.addEventListener("mouseleave",()=>{f.classList.add("tooltipped"),f.blur()},{once:!0})),d.dispatchEvent(new CustomEvent("details:toggled",{bubbles:!0,cancelable:!1,detail:{open:e}})),b&&d.dispatchEvent(new CustomEvent("details:toggled-group",{bubbles:!0,cancelable:!1,detail:{open:e,group:b}}))})})}function l(a){let b=a.getAttribute("data-details-container")||".js-details-container",c=a.closest(b),d=c.classList;return d.contains("Details--on")||d.contains("open")}function m(a){let b=!1,c=a.parentElement;for(;c;)c.classList.contains("Details-content--shown")&&(b=!0),c.classList.contains("js-details-container")&&(c.classList.toggle("open",!b),c.classList.toggle("Details--on",!b),b=!1),c=c.parentElement}(0,e.on)("click",".js-details-target",function(a){let b=a.altKey,c=a.currentTarget;k(c,{withGroup:b}),a.preventDefault()}),(0,d.Z)(function({target:a}){a&&m(a)})},81574(a,b,c){c.d(b,{Z:()=>h});var d=c(80721),e=c(45586);let f=[],g=0;function h(a){!async function(){f.push(a),await d.x,i()}()}function i(){let a=g;g=f.length,j(f.slice(a),null,window.location.href)}function j(a,b,c){let d=window.location.hash.slice(1),e=d?document.getElementById(d):null,f={oldURL:b,newURL:c,target:e};for(let g of a)g.call(null,f)}h.clear=()=>{f.length=g=0};let k=window.location.href;window.addEventListener("popstate",function(){k=window.location.href}),window.addEventListener("hashchange",function(a){let b=window.location.href;try{j(f,a.oldURL||k,b)}finally{k=b}});let l=null;document.addEventListener(e.QE.START,function(){l=window.location.href}),document.addEventListener(e.QE.SUCCESS,function(){j(f,l,window.location.href)})},20332(a,b,c){c.d(b,{h:()=>f});var d=c(59753),e=c(70763);function f(){let a=!1,b=document.getElementById("start-of-content");if(b){let c=b.nextElementSibling;if(c instanceof HTMLElement)return(a="1"===c.getAttribute("data-skipped-to-content"))&&c.removeAttribute("data-skipped-to-content"),a}}(0,d.on)("click",".js-skip-to-content",function(a){let b=document.getElementById("start-of-content");if(b){let c=b.nextElementSibling;c instanceof HTMLElement&&(c.setAttribute("tabindex","-1"),c.setAttribute("data-skipped-to-content","1"),c.focus())}a.preventDefault()});let g="ontouchstart"in document,h=document.querySelectorAll(".js-header-menu-item");for(let i of h)i.addEventListener("details:toggled",a=>{let b=a.target;if(a instanceof CustomEvent&&a.detail.open)for(let c of h)c!==b&&(0,e.Qp)(c,{force:!1})}),g||i.addEventListener("mouseleave",a=>{let b=a.target;b.classList.contains("open")&&(0,e.Qp)(b,{force:!1})});document.addEventListener("context-region-label:update",a=>{if(!(a instanceof CustomEvent&&a.detail.label))return;let b=document.querySelector(".js-context-region-label");b&&(b.textContent=a.detail.label)})},35002(a,b,c){c.d(b,{O3:()=>j,SX:()=>g,"_g":()=>h,a8:()=>f,lB:()=>i});let d=0,e=new Set;function f(a){e.add(a)}function g(a){e.delete(a)}function h(){return d}function i(a){for(let b of(d=a,a?document.body.style.setProperty("--base-sticky-header-height",`${a}px`):document.body.style.removeProperty("--base-sticky-header-height"),e))b(a)}let j="var(--base-sticky-header-height, 0px)"},21935(a,b,c){c.d(b,{H:()=>m});var d=c(20332),e=c(80721),f=c(64463),g=c(35002);let h=!1,i=[];function j(){i.length?k():l()}function k(){h||(window.addEventListener("resize",n),document.addEventListener("scroll",n),h=!0)}function l(){window.removeEventListener("resize",n),document.removeEventListener("scroll",n),h=!1}function m(){o(!0)}function n(){o()}function o(a=!1){for(let b of i)if(b.element.offsetHeight>0){let{element:c,placeholder:d,top:e}=b,f=c.getBoundingClientRect();if(d){let g=d.getBoundingClientRect();c.classList.contains("is-stuck")?g.top>x(c,e)?q(b):r(b):f.top<=x(c,e)?p(b):a&&r(b)}else{let h=.1;f.top-x(c,e)<h?p(b):q(b)}}}function p({element:a,placeholder:b,top:c}){if(b){let d=a.getBoundingClientRect();y(a,x(a,c)),a.style.left=`${d.left}px`,a.style.width=`${d.width}px`,a.style.marginTop="0",a.style.position="fixed",b.style.display="block"}a.classList.add("is-stuck")}function q({element:a,placeholder:b}){b&&(a.style.position="static",a.style.marginTop=b.style.marginTop,b.style.display="none"),a.classList.remove("is-stuck")}function r({element:a,placeholder:b,offsetParent:c,top:e}){if(b&&!(0,d.h)()){let f=a.getBoundingClientRect(),g=b.getBoundingClientRect();if(y(a,x(a,e)),a.style.left=`${g.left}px`,a.style.width=`${g.width}px`,c){let h=c.getBoundingClientRect();h.bottom<f.height+parseInt(String(e))&&(a.style.top=`${h.bottom-f.height}px`)}}}async function s(a){await e.C,requestAnimationFrame(()=>{(function(a){let b=function(a){if(function(a){let{position:b}=window.getComputedStyle(a);return/sticky/.test(b)}(a))return null;let b=a.previousElementSibling;if(b&&b.classList.contains("is-placeholder"))return b;let c=document.createElement("div");return c.style.visibility="hidden",c.style.display="none",c.style.height=window.getComputedStyle(a).height,c.className=a.className,c.classList.remove("js-sticky"),c.classList.add("is-placeholder"),a.parentNode.insertBefore(c,a)}(a),c=window.getComputedStyle(a).position;a.style.position="static";let d=a.offsetParent;a.style.position="fixed";let e=w(a),f={element:a,placeholder:b,offsetParent:d,top:"auto"===e?0:parseInt(e||"0")};a.style.position=c,i.push(f)})(a),o(),j()})}async function t(a){if(null===a.offsetParent)return;await e.C;let b=Math.floor(a.getBoundingClientRect().height);b>0&&((0,g.lB)(b),u(),m())}function u(){for(let a of document.querySelectorAll(".js-position-sticky, .js-notification-shelf-offset-top"))v(a)}function v(a){if(a.classList.contains("js-notification-top-shelf"))return;let b=parseInt(w(a))||0;y(a,b+(0,g._g)())}function w(a){let b=a.getAttribute("data-original-top");if(null!=b)return b;let c=window.getComputedStyle(a).top;return a.setAttribute("data-original-top",c),c}function x(a,b){return a.classList.contains("js-notification-top-shelf")?b:b+(0,g._g)()}function y(a,b){a.style.setProperty("top",`${b}px`,"important")}(0,f.N7)(".js-sticky",{constructor:HTMLElement,add(a){a.isConnected&&s(a)},remove(a){(function(a){let b=i.map(a=>a.element).indexOf(a);i.splice(b,1)})(a),j()}}),(0,f.N7)(".js-notification-top-shelf",{constructor:HTMLElement,add(a){t(a)},remove(){(0,g._g)()>0&&((0,g.lB)(0),u(),m())}}),(0,f.N7)(".js-notification-shelf-offset-top, .js-position-sticky",{constructor:HTMLElement,add:v})},87098(a,b,c){function d(a,b=location.hash){return e(a,f(b))}function e(a,b){return""===b?null:a.getElementById(b)||a.getElementsByName(b)[0]}function f(a){try{return decodeURIComponent(a.slice(1))}catch{return""}}c.d(b,{"$z":()=>f,Kt:()=>d,Q:()=>e})},3126(a,b,c){c.d(b,{kc:()=>g,lA:()=>h,zT:()=>f});var d=c(87098),e=c(21935);function f(a){if(a.hasAttribute("data-ignore-sticky-scroll"))return;let b=a.ownerDocument;setTimeout(()=>{b&&b.defaultView&&(a.scrollIntoView(),b.defaultView.scrollBy(0,-h(b)))},0)}function g(a){let b=(0,d.Kt)(a);b&&f(b)}function h(a){(0,e.H)();let b=a.querySelectorAll(".js-sticky-offset-scroll"),c=a.querySelectorAll(".js-position-sticky"),d=Math.max(0,...Array.from(b).map(a=>{let{top:b,height:c}=a.getBoundingClientRect();return 0===b?c:0}))+Math.max(0,...Array.from(c).map(a=>{let{top:b,height:c}=a.getBoundingClientRect(),d=parseInt(getComputedStyle(a).top);if(!a.parentElement)return 0;let e=a.parentElement.getBoundingClientRect().top;return b===d&&e<0?c:0})),f=a.querySelectorAll(".js-position-sticky-stacked"),g=Array.from(f).reduce((a,b)=>{let{height:c,top:d}=b.getBoundingClientRect(),e=b.classList.contains("is-stuck");return a+(!(d<0)&&e?c:0)},0);return d+g}}}])
//# sourceMappingURL=app_assets_modules_github_sticky-scroll-into-view_ts-27bacf305929.js.map