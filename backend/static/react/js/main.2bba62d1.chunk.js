(this["webpackJsonprbc-no-dnd"]=this["webpackJsonprbc-no-dnd"]||[]).push([[0],{23:function(e,n,t){e.exports=t(34)},28:function(e,n,t){},32:function(e,n,t){},34:function(e,n,t){"use strict";t.r(n);var o=t(0),i=t.n(o),a=t(3),r=t.n(a),c=(t(28),t(16)),s=t(8),l=t(4),u=t(21),f=t(22),d=t(12),h=t(13),v=t(20),g=t.n(v),w=(t(32),t(33),Object(d.b)(g.a)),b=function(e){console.log(e)},p=function(e){Object(f.a)(t,e);var n=Object(u.a)(t);function t(e){var o;return Object(c.a)(this,t),(o=n.call(this,e)).state={error:null,events:[]},o.requestAvailableDates=o.requestAvailableDates.bind(Object(l.a)(o)),o}return Object(s.a)(t,[{key:"requestAvailableDates",value:function(e){var n=this;fetch("/api/getavailability",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({start:e.start,end:e.end})}).then((function(e){return e.json()})).then((function(e){n.setState({events:e.events})}),(function(e){n.setState({error:e}),h.b.error("ERROR: "+JSON.stringify(e))}))}},{key:"render",value:function(){return i.a.createElement("div",{className:"App"},i.a.createElement(h.a,{position:"bottom-right"}),i.a.createElement(d.a,{localizer:w,defaultDate:new Date,defaultView:"month",events:this.state.events,views:["month"],style:{height:"100vh"},onRangeChange:this.requestAvailableDates,onSelectEvent:b}))}}]),t}(o.Component),m=Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));function y(e){navigator.serviceWorker.register(e).then((function(e){e.onupdatefound=function(){var n=e.installing;n.onstatechange=function(){"installed"===n.state&&(navigator.serviceWorker.controller?console.log("New content is available; please refresh."):console.log("Content is cached for offline use."))}}})).catch((function(e){console.error("Error during service worker registration:",e)}))}r.a.render(i.a.createElement(p,null),document.getElementById("root")),function(){if("serviceWorker"in navigator){if(new URL("/static/react",window.location).origin!==window.location.origin)return;window.addEventListener("load",(function(){var e="".concat("/static/react","/service-worker.js");m?(!function(e){fetch(e).then((function(n){404===n.status||-1===n.headers.get("content-type").indexOf("javascript")?navigator.serviceWorker.ready.then((function(e){e.unregister().then((function(){window.location.reload()}))})):y(e)})).catch((function(){console.log("No internet connection found. App is running in offline mode.")}))}(e),navigator.serviceWorker.ready.then((function(){console.log("This web app is being served cache-first by a service worker. To learn more, visit https://goo.gl/SC7cgQ")}))):y(e)}))}}()}},[[23,1,2]]]);
//# sourceMappingURL=main.2bba62d1.chunk.js.map