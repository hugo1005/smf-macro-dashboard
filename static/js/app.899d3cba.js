(function(t){function e(e){for(var r,s,i=e[0],l=e[1],c=e[2],u=0,f=[];u<i.length;u++)s=i[u],Object.prototype.hasOwnProperty.call(n,s)&&n[s]&&f.push(n[s][0]),n[s]=0;for(r in l)Object.prototype.hasOwnProperty.call(l,r)&&(t[r]=l[r]);h&&h(e);while(f.length)f.shift()();return o.push.apply(o,c||[]),a()}function a(){for(var t,e=0;e<o.length;e++){for(var a=o[e],r=!0,s=1;s<a.length;s++){var l=a[s];0!==n[l]&&(r=!1)}r&&(o.splice(e--,1),t=i(i.s=a[0]))}return t}var r={},n={app:0},o=[];function s(t){return i.p+"js/"+({about:"about"}[t]||t)+"."+{about:"21f95d79"}[t]+".js"}function i(e){if(r[e])return r[e].exports;var a=r[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,i),a.l=!0,a.exports}i.e=function(t){var e=[],a=n[t];if(0!==a)if(a)e.push(a[2]);else{var r=new Promise((function(e,r){a=n[t]=[e,r]}));e.push(a[2]=r);var o,l=document.createElement("script");l.charset="utf-8",l.timeout=120,i.nc&&l.setAttribute("nonce",i.nc),l.src=s(t);var c=new Error;o=function(e){l.onerror=l.onload=null,clearTimeout(u);var a=n[t];if(0!==a){if(a){var r=e&&("load"===e.type?"missing":e.type),o=e&&e.target&&e.target.src;c.message="Loading chunk "+t+" failed.\n("+r+": "+o+")",c.name="ChunkLoadError",c.type=r,c.request=o,a[1](c)}n[t]=void 0}};var u=setTimeout((function(){o({type:"timeout",target:l})}),12e4);l.onerror=l.onload=o,document.head.appendChild(l)}return Promise.all(e)},i.m=t,i.c=r,i.d=function(t,e,a){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(i.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)i.d(a,r,function(e){return t[e]}.bind(null,r));return a},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/",i.oe=function(t){throw console.error(t),t};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],c=l.push.bind(l);l.push=e,l=l.slice();for(var u=0;u<l.length;u++)e(l[u]);var h=c;o.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"034f":function(t,e,a){"use strict";a("85ec")},1:function(t,e){},"1e45":function(t,e,a){"use strict";a("8940")},"56d7":function(t,e,a){"use strict";a.r(e);a("e260"),a("e6cf"),a("cca6"),a("a79d");var r=a("2b0e"),n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"app"}},[t._m(0),a("div",{attrs:{id:"macro-bg"}},[t._m(1),t.loading?t._e():a("div",{attrs:{id:"chart-container"}},t._l(Object.keys(t.data),(function(e){return a("div",{key:e},[a("LineChart",{staticClass:"chart",attrs:{category:e.split("_")[0],title:e.split("_").slice(1).join(" "),data:t.data[e]}})],1)})),0)]),t._m(2),t.loading_risk?t._e():a("div",{staticClass:"padded"},[a("h2",[t._v(" Portfolio Summary ")]),a("table",[a("th",[t._v("Alpha")]),a("th",[t._v("Beta")]),a("th",[t._v("Sharpe")]),a("th",[t._v("Tracking Error (%)")]),a("tr",[a("td",[t._v(t._s(t.risk.portfolio_summary_stats.alpha))]),a("td",[t._v(t._s(t.risk.portfolio_summary_stats.beta))]),a("td",[t._v(t._s(t.risk.portfolio_summary_stats.sharpe))]),a("td",[t._v(t._s(t.risk.portfolio_summary_stats.tracking_error_pct))])])]),a("h2",[t._v(" Region Attribution ")]),a("table",[a("th",[t._v("Region")]),a("th",[t._v("Benchmark Total Return")]),a("th",[t._v("Portfolio Total Return")]),a("th",[t._v("Portfolio Outperformance")]),a("th",[t._v("Selection Effect")]),a("th",[t._v("Allocation Effect")]),a("th",[t._v("Total Effect")]),t._l(Object.entries(t.risk.attribution.regions),(function(e){var r=e[0],n=e[1];return a("tr",{key:r},[a("td",[t._v(t._s(r))]),a("td",[t._v(t._s(n["Benchmark Total Return"]))]),a("td",[t._v(t._s(n["Portfolio Total Return"]))]),a("td",[t._v(t._s(n["Portfolio Outperformance"]))]),a("td",[t._v(t._s(n["Selection Effect"]))]),a("td",[t._v(t._s(n["Allocation Effect"]))]),a("td",[t._v(t._s(n["Total Effect"]))])])}))],2),a("h2",[t._v(" Sector Attribution ")]),a("table",[a("th",[t._v("Sector")]),a("th",[t._v("Allocation Effect (EU)")]),a("th",[t._v("Allocation Effect (US)")]),a("th",[t._v("Selection Effect (EU)")]),a("th",[t._v("Selection Effect (US)")]),a("th",[t._v("Total Effect (EU)")]),a("th",[t._v("Total Effect (US)")]),t._l(Object.entries(t.risk.attribution.sectors),(function(e){var r=e[0],n=e[1];return a("tr",{key:r},[a("td",[t._v(t._s(r))]),a("td",[t._v(t._s(t.roundToTwo(n["Allocation_EU"])))]),a("td",[t._v(t._s(t.roundToTwo(n["Allocation_US"])))]),a("td",[t._v(t._s(t.roundToTwo(n["Selection_EU"])))]),a("td",[t._v(t._s(t.roundToTwo(n["Selection_US"])))]),a("td",[t._v(t._s(t.roundToTwo(n["Allocation_EU"]+n["Selection_EU"])))]),a("td",[t._v(t._s(t.roundToTwo(n["Allocation_US"]+n["Selection_US"])))])])}))],2)])])},o=[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"padded",attrs:{id:"banner"}},[r("img",{attrs:{src:a("7d33")}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"chart-header"}},[a("h1",[t._v(" Macro Overview ")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"chart-header"}},[a("h1",[t._v(" Risk Dashboard ")])])}],s=(a("4160"),a("b64b"),a("159b"),function(){var t=this,e=t.$createElement,a=t._self._c||e;return t.loading?t._e():a("div",[a("h1",[a("span",{style:{color:t.highlight[t.category]}},[t._v(t._s(t.category))]),t._v(t._s(t.title))]),a("svg",{style:{"background-image":"linear-gradient("+t.background[t.category]+"00,"+t.background[t.category]+")"},attrs:{width:t.chartDefaults.width+t.chartDefaults.margin.left+t.chartDefaults.margin.right,height:t.chartDefaults.height+t.chartDefaults.margin.top+t.chartDefaults.margin.bottom}},[a("g",{staticClass:"lineChart",attrs:{transform:t.translate}},[a("axis",{staticClass:"yA",attrs:{scales:t.getScales().yAxis,chartDefaults:t.chartDefaults,data:t.data,trns:t.trnsY}}),a("axis",{staticClass:"xA",attrs:{scales:t.getScales().xAxis,chartDefaults:t.chartDefaults,data:t.data,trns:t.trnsX()}}),a("path",{staticClass:"line",attrs:{d:t.line}}),a("circle",{attrs:{cx:t.getScales().x(t.data[this.data.length-1].date),cy:t.getScales().y(t.data[this.data.length-1].value),r:"3",fill:"#fff"}}),a("text",{staticStyle:{"font-size":"10px"},attrs:{x:t.getScales().x(t.data[this.data.length-1].date),y:t.getScales().y(t.data[this.data.length-1].value),fill:t.highlight[t.category],dx:"-10",dy:"-10"}},[t._v(t._s(t.roundData(t.data[this.data.length-1].value,2)))])],1)])])}),i=[],l=(a("a623"),a("5698")),c=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("g",{attrs:{transform:t.trns}},[a("g",{ref:"axis"})])},u=[],h={name:"axis",props:{scales:Function,chartDefaults:Object,data:Array,trns:String},data:function(){return{width:0,height:0}},mounted:function(){var t=this.$refs.axis;l["g"](t).call(this.scales)}},f=h,d=(a("1e45"),a("2877")),v=Object(d["a"])(f,c,u,!1,null,null,null),_=v.exports,g=a("bc3a"),p=a.n(g),m=a("7909"),b={name:"vue-line-chart",components:{axis:_},props:["title","data","category"],data:function(){return{loading:!0,chartDefaults:{width:160,height:100,chartId:"linechart-vue",margin:{top:5,right:0,bottom:30,left:50},gridOpacity:1,data:[]},background:{BOND:"#AD3B3B","FX|COMMODITY":"#86AD3B",INDEX:"#3BA9AD",METRIC:"#743BAD",COMMODITITY:"#AD3BA0",SURVEY:"#3B51AD"},highlight:{BOND:"#E55151","FX|COMMODITY":"#A7D64B",INDEX:"#4CCED3",METRIC:"#B47CEB",COMMODITITY:"#AD3BA0",SURVEY:"#6B84EB"},line:"",translate:"translate(35,5)",trnsY:"translate(0,0)",trnsX:this.getTrnsx,toggleClass:!0}},created:function(){this.calculatePath(),this.loading=!1},methods:{roundData:function(t,e){return Object(m["a"])(t,e)},getScales:function(){console.log("Drawing scales..."),console.log(this.data[0].date);var t=l["c"](this.data,(function(t){return t.value})),e=l["f"]().domain(l["c"](this.data,(function(t){return t.date}))).rangeRound([0,this.chartDefaults.width-0*this.chartDefaults.width]),a=l["e"]().domain([t[0]-.2*(t[1]-t[0]),t[1]+.2*(t[1]-t[0])]).range([this.chartDefaults.height,0]);l["a"]().scale(e),l["b"]().scale(a);var r=l["a"]().scale(e).ticks(l["i"].every(4)).tickFormat(l["h"]("%b-%y")),n=l["b"]().scale(a).ticks(5),o=l["b"]().scale(a).tickSize(-(this.chartDefaults.width-100),0,0).tickFormat("");return{x:e,y:a,xAxis:r,yAxis:n,yGrid:o}},getTrnsx:function(t){var e="translate(0,"+this.chartDefaults.height+")";return e},calculatePath:function(){console.log("Drawing path");var t=this.getScales(),e=l["d"]().x((function(e){return t.x(e.date)})).y((function(e){return t.y(e.value)}));this.line=e(this.data)}}},y=b,k=(a("f968"),Object(d["a"])(y,s,i,!1,null,null,null)),E=k.exports,x={name:"App",components:{LineChart:E},data:function(){return{data:{},loading:!0,risk:{},loading_risk:!0}},methods:{roundToTwo:function(t){return+(Math.round(t+"e+2")+"e-2")}},created:function(){var t=this,e="http://localhost:5000/chart_data";p.a.get(e).then((function(e){console.log("Recieved data..."),t.data=e.data;var a=l["j"]("%Y-%m-%d");Object.keys(t.data).forEach((function(e){t.data[e].forEach((function(t){t.date=a(t.date)}))})),console.log("Recieved data..."),t.loading=!1})).catch((function(t){console.error(t)}));var a="http://localhost:5000/risk_data";p.a.get(a).then((function(e){console.log("Recieved data..."),t.risk=e.data,t.loading_risk=!1})).catch((function(t){console.error(t)}))}},j=x,D=(a("034f"),Object(d["a"])(j,n,o,!1,null,null,null)),w=D.exports,S=(a("d3b7"),a("8c4f")),T=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"home"},[r("img",{attrs:{alt:"Vue logo",src:a("cf05")}}),r("HelloWorld",{attrs:{msg:"Welcome to Your Vue.js App"}})],1)},O=[],A=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"hello"},[a("h1",[t._v(t._s(t.msg))]),t._m(0),a("h3",[t._v("Installed CLI Plugins")]),t._m(1),a("h3",[t._v("Essential Links")]),t._m(2),a("h3",[t._v("Ecosystem")]),t._m(3)])},C=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("p",[t._v(" For a guide and recipes on how to configure / customize this project,"),a("br"),t._v(" check out the "),a("a",{attrs:{href:"https://cli.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vue-cli documentation")]),t._v(". ")])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel",target:"_blank",rel:"noopener"}},[t._v("babel")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-router",target:"_blank",rel:"noopener"}},[t._v("router")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint",target:"_blank",rel:"noopener"}},[t._v("eslint")])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://vuejs.org",target:"_blank",rel:"noopener"}},[t._v("Core Docs")])]),a("li",[a("a",{attrs:{href:"https://forum.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("Forum")])]),a("li",[a("a",{attrs:{href:"https://chat.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("Community Chat")])]),a("li",[a("a",{attrs:{href:"https://twitter.com/vuejs",target:"_blank",rel:"noopener"}},[t._v("Twitter")])]),a("li",[a("a",{attrs:{href:"https://news.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("News")])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://router.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vue-router")])]),a("li",[a("a",{attrs:{href:"https://vuex.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vuex")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-devtools#vue-devtools",target:"_blank",rel:"noopener"}},[t._v("vue-devtools")])]),a("li",[a("a",{attrs:{href:"https://vue-loader.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vue-loader")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/awesome-vue",target:"_blank",rel:"noopener"}},[t._v("awesome-vue")])])])}],M={name:"HelloWorld",props:{msg:String}},P=M,B=(a("c1c7"),Object(d["a"])(P,A,C,!1,null,"25d525f8",null)),U=B.exports,R={name:"Home",components:{HelloWorld:U}},$=R,I=Object(d["a"])($,T,O,!1,null,null,null),Y=I.exports,F=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},[t._v(" "+t._s(t.msg)+" ")])},L=[],X={name:"Ping",data:function(){return{msg:""}},methods:{getMessage:function(){var t=this,e="http://localhost:5000/ping";p.a.get(e).then((function(e){t.msg=e.data})).catch((function(t){console.error(t)}))}},created:function(){this.getMessage()}},H=X,N=Object(d["a"])(H,F,L,!1,null,null,null),V=N.exports;r["a"].use(S["a"]);var W=[{path:"/",name:"Home",component:Y},{path:"/ping",name:"Ping",component:V},{path:"/about",name:"About",component:function(){return a.e("about").then(a.bind(null,"f820"))}}],z=new S["a"]({mode:"history",base:"/",routes:W}),J=z;r["a"].config.productionTip=!1,new r["a"]({router:J,render:function(t){return t(w)}}).$mount("#app")},"7d33":function(t,e,a){t.exports=a.p+"img/SMF_A_plain@3x.76fb46f1.png"},"85ec":function(t,e,a){},8940:function(t,e,a){},a324:function(t,e,a){},c1c7:function(t,e,a){"use strict";a("fe5e")},cf05:function(t,e,a){t.exports=a.p+"img/logo.82b9c7a5.png"},f968:function(t,e,a){"use strict";a("a324")},fe5e:function(t,e,a){}});
//# sourceMappingURL=app.899d3cba.js.map