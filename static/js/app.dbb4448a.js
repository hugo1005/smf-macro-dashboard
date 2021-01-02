(function(t){function e(e){for(var r,i,o=e[0],c=e[1],l=e[2],u=0,h=[];u<o.length;u++)i=o[u],Object.prototype.hasOwnProperty.call(s,i)&&s[i]&&h.push(s[i][0]),s[i]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(t[r]=c[r]);f&&f(e);while(h.length)h.shift()();return n.push.apply(n,l||[]),a()}function a(){for(var t,e=0;e<n.length;e++){for(var a=n[e],r=!0,i=1;i<a.length;i++){var c=a[i];0!==s[c]&&(r=!1)}r&&(n.splice(e--,1),t=o(o.s=a[0]))}return t}var r={},s={app:0},n=[];function i(t){return o.p+"js/"+({about:"about"}[t]||t)+"."+{about:"21f95d79"}[t]+".js"}function o(e){if(r[e])return r[e].exports;var a=r[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,o),a.l=!0,a.exports}o.e=function(t){var e=[],a=s[t];if(0!==a)if(a)e.push(a[2]);else{var r=new Promise((function(e,r){a=s[t]=[e,r]}));e.push(a[2]=r);var n,c=document.createElement("script");c.charset="utf-8",c.timeout=120,o.nc&&c.setAttribute("nonce",o.nc),c.src=i(t);var l=new Error;n=function(e){c.onerror=c.onload=null,clearTimeout(u);var a=s[t];if(0!==a){if(a){var r=e&&("load"===e.type?"missing":e.type),n=e&&e.target&&e.target.src;l.message="Loading chunk "+t+" failed.\n("+r+": "+n+")",l.name="ChunkLoadError",l.type=r,l.request=n,a[1](l)}s[t]=void 0}};var u=setTimeout((function(){n({type:"timeout",target:c})}),12e4);c.onerror=c.onload=n,document.head.appendChild(c)}return Promise.all(e)},o.m=t,o.c=r,o.d=function(t,e,a){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(o.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)o.d(a,r,function(e){return t[e]}.bind(null,r));return a},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="/",o.oe=function(t){throw console.error(t),t};var c=window["webpackJsonp"]=window["webpackJsonp"]||[],l=c.push.bind(c);c.push=e,c=c.slice();for(var u=0;u<c.length;u++)e(c[u]);var f=l;n.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"034f":function(t,e,a){"use strict";a("85ec")},1:function(t,e){},"1e45":function(t,e,a){"use strict";a("8940")},"56d7":function(t,e,a){"use strict";a.r(e);a("e260"),a("e6cf"),a("cca6"),a("a79d");var r=a("2b0e"),s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"app"}},[t._m(0),a("div",{staticClass:"macro-bg"},[t._m(1),t.loading?t._e():a("div",{attrs:{id:"chart-container"}},t._l(Object.keys(t.data),(function(e){return a("div",{key:e},[a("LineChart",{staticClass:"chart",attrs:{category:e.split("_")[0],title:e.split("_").slice(1).join(" "),data:t.data[e],background:t.background_macro,highlight:t.highlight_macro,month_tick_interval:4}})],1)})),0)]),a("div",{staticClass:"macro-bg"},[t._m(2),t.loading_risk?t._e():a("div",{staticClass:"padded"},[a("div",{staticClass:"dash-panel"},[a("div",{attrs:{id:"port-stats"}},[a("h2",[t._v("PORTFOLIO STATISTICS")]),a("div",{attrs:{id:"port-stats-data"}},[a("div",{staticClass:"port-stat"},[a("div",{staticClass:"port-stat-name"},[t._v("ALPHA")]),a("div",{staticClass:"port-stat-value"},[t._v(t._s(t.risk.portfolio_summary_stats.alpha))])]),a("div",{staticClass:"port-stat"},[a("div",{staticClass:"port-stat-name"},[t._v("BETA")]),a("div",{staticClass:"port-stat-value"},[t._v(t._s(t.risk.portfolio_summary_stats.beta))])]),a("div",{staticClass:"port-stat"},[a("div",{staticClass:"port-stat-name"},[t._v("SHARPE")]),a("div",{staticClass:"port-stat-value"},[t._v(t._s(t.risk.portfolio_summary_stats.sharpe))])]),a("div",{staticClass:"port-stat"},[a("div",{staticClass:"port-stat-name"},[t._v("TRACKING ERROR")]),a("div",{staticClass:"port-stat-value"},[t._v(t._s(t.risk.portfolio_summary_stats.tracking_error_pct)+"%")])])])]),a("div",{attrs:{id:"port-attribution-panel"}},[a("h2",[t._v("RETURN ATTRIBUTION SCORING")]),a("div",{attrs:{id:"attr-data"}},[a("div",{staticClass:"attr-stat"},[t._m(3),t._l(t.effects,(function(e){return a("div",{key:e,staticClass:"attr-stat-box-label"},[a("svg",{attrs:{width:"100%",height:"100%"}},[a("rect",{attrs:{width:"100%",height:"100%",fill:"#A84E4E70"}}),a("text",{attrs:{fill:"#FF1414","font-size":"14","text-anchor":"middle",transform:"translate(20,60) rotate(270 0 0)"}},[t._v(t._s(t.effects_map[e]))])])])}))],2),t._l(t.regions.map((function(e){return[e,t.risk.attribution.regions[e]]})),(function(e){var r=e[0],s=e[1];return a("div",{key:r,staticClass:"attr-stat border-left"},[a("h3",{staticClass:"attr-stat-head"},[a("span",{staticStyle:{color:"#92cbf1"}},[t._v(t._s(s["Benchmark Total Return"])+"% RETURN")]),a("br"),a("span",{staticStyle:{color:"#ffffff90"}},[t._v(t._s(t.regions_short[r])+" INDEX")])]),t._l(t.effects,(function(e){return a("div",{key:e,staticClass:"attr-stat-box"},[a("svg",{attrs:{width:"100%",height:"100%"}},[a("defs",[a("linearGradient",{attrs:{id:"gradPos",x1:"0%",y1:"0%",x2:"0%",y2:"100%"}},[a("stop",{staticStyle:{"stop-color":"#86AD3B","stop-opacity":"1"},attrs:{offset:"0%"}}),a("stop",{staticStyle:{"stop-color":"#A7D64B","stop-opacity":"0.3"},attrs:{offset:"100%"}})],1),a("linearGradient",{attrs:{id:"gradNeg",x1:"0%",y1:"0%",x2:"0%",y2:"100%"}},[a("stop",{staticStyle:{"stop-color":"#AD3B3B","stop-opacity":"1"},attrs:{offset:"0%"}}),a("stop",{staticStyle:{"stop-color":"#E55151","stop-opacity":"0.3"},attrs:{offset:"100%"}})],1)],1),a("circle",{attrs:{r:t.getPctAttributionRadius(s[e],t.risk.attribution.regions),fill:t.getAttributionGrad(s[e]),cx:"50%",cy:"50%"}}),a("text",{attrs:{x:"4%",y:"96%",fill:"#ffffff90","text-anchor":"right","dominant-baseline":"top"}},[t._v(t._s(s[e])+"%")])])])})),a("h3",{staticClass:"attr-stat-head"},[a("span",{style:{color:t.getAttributionColor(s["Portfolio Total Return"])}},[t._v(t._s(s["Portfolio Total Return"])+"% RETURN")]),a("br"),a("span",{staticStyle:{color:"#fff"}},[t._v(t._s(t.regions_short[r])+" PORTFOLIO")])])],2)}))],2)])]),t._l(Object.entries(t.risk.attribution.sectors),(function(e){var r=e[0],s=e[1];return a("div",{key:r,attrs:{id:"port-attribution-panel"}},[a("h2",[t._v(t._s(t.regions_short[r])+" SECTOR ATTRIBUTION SCORING")]),a("div",{attrs:{id:"attr-data"}},[a("div",{staticClass:"attr-stat"},[t._m(4,!0),t._l(t.effects,(function(e){return a("div",{key:e,staticClass:"attr-stat-box-label"},[a("svg",{attrs:{width:"100%",height:"100%"}},[a("rect",{attrs:{width:"100%",height:"100%",fill:"#A84E4E70"}}),a("text",{attrs:{fill:"#FF1414","font-size":"14","text-anchor":"middle",transform:"translate(20,60) rotate(270 0 0)"}},[t._v(t._s(t.effects_map[e]))])])])}))],2),t._l(Object.entries(s),(function(e){var r=e[0],n=e[1];return a("div",{key:r,staticClass:"attr-stat border-left"},[a("h3",{staticClass:"attr-stat-head"},[a("span",{staticStyle:{color:"#92cbf1"}},[t._v(t._s(n["Benchmark Total Return"])+"% RETURN")]),a("br"),a("span",{staticStyle:{color:"#ffffff90"}},[t._v(t._s(t.sectors_short[r])+" INDEX")])]),t._l(t.effects,(function(e){return a("div",{key:e,staticClass:"attr-stat-box"},[a("svg",{attrs:{width:"100%",height:"100%"}},[a("defs",[a("linearGradient",{attrs:{id:"gradPos",x1:"0%",y1:"0%",x2:"0%",y2:"100%"}},[a("stop",{staticStyle:{"stop-color":"#86AD3B","stop-opacity":"1"},attrs:{offset:"0%"}}),a("stop",{staticStyle:{"stop-color":"#A7D64B","stop-opacity":"0.3"},attrs:{offset:"100%"}})],1),a("linearGradient",{attrs:{id:"gradNeg",x1:"0%",y1:"0%",x2:"0%",y2:"100%"}},[a("stop",{staticStyle:{"stop-color":"#AD3B3B","stop-opacity":"1"},attrs:{offset:"0%"}}),a("stop",{staticStyle:{"stop-color":"#E55151","stop-opacity":"0.3"},attrs:{offset:"100%"}})],1)],1),a("circle",{attrs:{r:t.getPctAttributionRadius(n[e],s),fill:t.getAttributionGrad(n[e]),cx:"50%",cy:"50%"}}),a("text",{attrs:{x:"4%",y:"96%",fill:"#ffffff90","text-anchor":"right","dominant-baseline":"top"}},[t._v(t._s(n[e])+"%")])])])})),a("h3",{staticClass:"attr-stat-head"},[a("span",{style:{color:t.getAttributionColor(n["Portfolio Total Return"])}},[t._v(t._s(n["Portfolio Total Return"])+"% RETURN")]),a("br"),a("span",{staticStyle:{color:"#fff"}},[t._v(t._s(t.sectors_short[r])+" PORTFOLIO")])])],2)}))],2)])}))],2)]),a("div",{staticClass:"macro-bg"},[t._m(5),t.loading_risk?t._e():a("div",{attrs:{id:"chart-container"}},t._l(Object.keys(t.risk.equities),(function(e){return a("div",{key:e},[a("LineChart",{staticClass:"chart",attrs:{category:e.split("_")[0],title:e.split("_").slice(1).join(" "),data:t.risk.equities[e],background:t.background_equities,highlight:t.highlight_equities,month_tick_interval:1,show_pct:!0,short_category:t.short_equities}})],1)})),0)])])},n=[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"padded",attrs:{id:"banner"}},[r("img",{attrs:{src:a("7d33")}}),r("img",{attrs:{src:a("99ad")}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"chart-header"}},[a("h1",[t._v(" Macro Overview ")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"chart-header"}},[a("h1",[t._v(" Risk Dashboard ")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("h3",{staticClass:"attr-stat-head"},[a("span",{staticStyle:{color:"#FF1414"}},[a("br")]),a("br"),a("span",{staticStyle:{color:"#ffffff90"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("h3",{staticClass:"attr-stat-head"},[a("span",{staticStyle:{color:"#FF1414"}},[a("br")]),a("br"),a("span",{staticStyle:{color:"#ffffff90"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"chart-header"}},[a("h1",[t._v(" Equity Charts ")])])}],i=(a("0481"),a("4160"),a("d81d"),a("4069"),a("b64b"),a("07ac"),a("159b"),a("2909")),o=function(){var t=this,e=t.$createElement,a=t._self._c||e;return t.loading?t._e():a("div",[a("h1",[a("span",{style:{color:t.highlight[t.category]}},[t._v(t._s(t.getShortendedCategory(t.category)))]),t._v(t._s(t.title)+" "),t.show_pct?a("span",{staticClass:"float-right",style:{color:t.getAttributionColor(t.getPctChange())}},[t._v("["+t._s(t.getPctChange())+" %]")]):t._e()]),a("svg",{style:{"background-image":"linear-gradient("+t.background[t.category]+"00,"+t.background[t.category]+")"},attrs:{width:t.chartDefaults.width+t.chartDefaults.margin.left+t.chartDefaults.margin.right,height:t.chartDefaults.height+t.chartDefaults.margin.top+t.chartDefaults.margin.bottom}},[a("g",{staticClass:"lineChart",attrs:{transform:t.translate}},[a("axis",{staticClass:"yA",attrs:{scales:t.getScales().yAxis,chartDefaults:t.chartDefaults,data:t.data,trns:t.trnsY}}),a("axis",{staticClass:"xA",attrs:{scales:t.getScales().xAxis,chartDefaults:t.chartDefaults,data:t.data,trns:t.trnsX()}}),a("path",{staticClass:"line",attrs:{d:t.line}}),a("circle",{attrs:{cx:t.getScales().x(t.data[this.data.length-1].date),cy:t.getScales().y(t.data[this.data.length-1].value),r:"3",fill:"#fff"}}),a("text",{staticStyle:{"font-size":"10px"},attrs:{x:t.getScales().x(t.data[this.data.length-1].date),y:t.getScales().y(t.data[this.data.length-1].value),fill:t.highlight[t.category],dx:"-10",dy:"-10"}},[t._v(t._s(t.roundData(t.data[this.data.length-1].value,2)))])],1)])])},c=[],l=(a("a623"),a("5698")),u=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("g",{attrs:{transform:t.trns}},[a("g",{ref:"axis"})])},f=[],h={name:"axis",props:{scales:Function,chartDefaults:Object,data:Array,trns:String},data:function(){return{width:0,height:0}},mounted:function(){var t=this.$refs.axis;l["g"](t).call(this.scales)}},d=h,g=(a("1e45"),a("2877")),p=Object(g["a"])(d,u,f,!1,null,null,null),v=p.exports,_=a("bc3a"),m=a.n(_),b=a("7909"),E={name:"vue-line-chart",components:{axis:v},props:["title","data","category","background","highlight","month_tick_interval","show_pct","short_category"],data:function(){return{loading:!0,chartDefaults:{width:160,height:100,chartId:"linechart-vue",margin:{top:5,right:0,bottom:30,left:50},gridOpacity:1,data:[]},line:"",translate:"translate(35,5)",trnsY:"translate(0,0)",trnsX:this.getTrnsx,toggleClass:!0}},created:function(){this.calculatePath(),this.loading=!1},methods:{getShortendedCategory:function(t){return this.short_category?this.short_category[t]:t},getAttributionColor:function(t){return t>=0?"#86AD3B":"#AD3B3B"},roundData:function(t,e){return Object(b["a"])(t,e)},getPctChange:function(){var t=this.data[this.data.length-1].value,e=this.data[0].value,a=100*(t/e-1);return this.roundData(a,2)},getScales:function(){console.log("Drawing scales..."),console.log(this.data[0].date);var t=l["c"](this.data,(function(t){return t.value})),e=l["f"]().domain(l["c"](this.data,(function(t){return t.date}))).rangeRound([0,this.chartDefaults.width-0*this.chartDefaults.width]),a=l["e"]().domain([t[0]-.2*(t[1]-t[0]),t[1]+.2*(t[1]-t[0])]).range([this.chartDefaults.height,0]);l["a"]().scale(e),l["b"]().scale(a);var r=l["a"]().scale(e).ticks(l["i"].every(this.month_tick_interval)).tickFormat(l["h"]("%b-%y")),s=l["b"]().scale(a).ticks(5),n=l["b"]().scale(a).tickSize(-(this.chartDefaults.width-100),0,0).tickFormat("");return{x:e,y:a,xAxis:r,yAxis:s,yGrid:n}},getTrnsx:function(t){var e="translate(0,"+this.chartDefaults.height+")";return e},calculatePath:function(){console.log("Drawing path");var t=this.getScales(),e=l["d"]().x((function(e){return t.x(e.date)})).y((function(e){return t.y(e.value)}));this.line=e(this.data)}}},C=E,y=(a("f968"),Object(g["a"])(C,o,c,!1,null,null,null)),A=y.exports,S={name:"App",components:{LineChart:A},data:function(){return{data:{},loading:!0,risk:{},loading_risk:!0,effects:["Selection Effect","Allocation Effect","Total Effect"],effects_map:{"Selection Effect":"Selection Effect","Allocation Effect":"Allocation Effect","Total Effect":"Outperformance"},regions:["Overall","US","Europe"],regions_short:{Overall:"OVERALL",US:"US",Europe:"EU"},sectors_short:{Communications:"COMMS",Consumer_Disrectionary:"DISC.",Consumer_Staples:"STAPLES",Energy_Renewables:"ENERGY",Financials:"FINANCIALS",Health_Care:"HEALTHCARE",Information_Technology:"TECH",Industrials:"INDUSTRIALS",Utilities:"UTILITIES",Other:"OTHER"},background_macro:{BOND:"#AD3B3B","FX|COMMODITY":"#86AD3B",INDEX:"#3BA9AD",METRIC:"#743BAD",COMMODITITY:"#AD3BA0",SURVEY:"#3B51AD"},highlight_macro:{BOND:"#E55151","FX|COMMODITY":"#A7D64B",INDEX:"#4CCED3",METRIC:"#B47CEB",COMMODITITY:"#AD3BA0",SURVEY:"#6B84EB"},highlight_equities:{COMMUNICATIONS:"#E55151","CONSUMER DISRECTIONARY":"#A7D64B","CONSUMER STAPLES":"#4CCED3","ENERGY RENEWABLES":"#B47CEB",FINANCIALS:"#AD3BA0","HEALTH CARE":"#6B84EB","INFORMATION TECHNOLOGY":"#E5AC51",INDUSTRIALS:"#4BD6A6",UTILITIES:"#EFADEF",OTHER:"#B47CEB"},background_equities:{COMMUNICATIONS:"#AD3B3B","CONSUMER DISRECTIONARY":"#86AD3B","CONSUMER STAPLES":"#3BA9AD","ENERGY RENEWABLES":"#743BAD",FINANCIALS:"#AD3BA0","HEALTH CARE":"#3B51AD","INFORMATION TECHNOLOGY":"#AD8A3B",INDUSTRIALS:"#3BAD70",UTILITIES:"#C904AB",OTHER:"#743BAD"},short_equities:{COMMUNICATIONS:"COMMS","CONSUMER DISRECTIONARY":"DISC.","CONSUMER STAPLES":"STAPLES","ENERGY RENEWABLES":"ENERGY",FINANCIALS:"FINANCIALS","HEALTH CARE":"HEALTHCARE","INFORMATION TECHNOLOGY":"TECH",INDUSTRIALS:"INDUSTRIALS",UTILITIES:"UTILITIES",OTHER:"OTHER"}}},methods:{roundToTwo:function(t){return+(Math.round(t+"e+2")+"e-2")},getPctAttributionRadius:function(t,e){var a=this,r=Object.values(e),s=r.map((function(t){return a.effects.map((function(e){return t[e]}))})).flat(),n=Math.max.apply(Math,Object(i["a"])(s)),o=t/n;return Math.abs(30*o)+"%"},getAttributionGrad:function(t){return t>=0?"url(#gradPos)":"url(#gradNeg)"},getAttributionColor:function(t){return t>=0?"#86AD3B":"#AD3B3B"}},created:function(){var t=this,e="./chart_data";m.a.get(e).then((function(e){console.log("Recieved data..."),t.data=e.data;var a=l["j"]("%Y-%m-%d");Object.keys(t.data).forEach((function(e){t.data[e].forEach((function(t){t.date=a(t.date)}))})),console.log("Recieved data..."),t.loading=!1})).catch((function(t){console.error(t)}));var a="./risk_data";m.a.get(a).then((function(e){console.log("Recieved data..."),t.risk=e.data;var a=l["j"]("%Y-%m-%d");Object.keys(t.risk.equities).forEach((function(e){t.risk.equities[e].forEach((function(t){t.date=a(t.date)}))})),t.loading_risk=!1})).catch((function(t){console.error(t)}))}},O=S,T=(a("034f"),Object(g["a"])(O,s,n,!1,null,null,null)),I=T.exports,R=(a("d3b7"),a("8c4f")),k=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"home"},[r("img",{attrs:{alt:"Vue logo",src:a("cf05")}}),r("HelloWorld",{attrs:{msg:"Welcome to Your Vue.js App"}})],1)},D=[],x=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"hello"},[a("h1",[t._v(t._s(t.msg))]),t._m(0),a("h3",[t._v("Installed CLI Plugins")]),t._m(1),a("h3",[t._v("Essential Links")]),t._m(2),a("h3",[t._v("Ecosystem")]),t._m(3)])},N=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("p",[t._v(" For a guide and recipes on how to configure / customize this project,"),a("br"),t._v(" check out the "),a("a",{attrs:{href:"https://cli.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vue-cli documentation")]),t._v(". ")])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel",target:"_blank",rel:"noopener"}},[t._v("babel")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-router",target:"_blank",rel:"noopener"}},[t._v("router")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint",target:"_blank",rel:"noopener"}},[t._v("eslint")])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://vuejs.org",target:"_blank",rel:"noopener"}},[t._v("Core Docs")])]),a("li",[a("a",{attrs:{href:"https://forum.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("Forum")])]),a("li",[a("a",{attrs:{href:"https://chat.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("Community Chat")])]),a("li",[a("a",{attrs:{href:"https://twitter.com/vuejs",target:"_blank",rel:"noopener"}},[t._v("Twitter")])]),a("li",[a("a",{attrs:{href:"https://news.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("News")])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://router.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vue-router")])]),a("li",[a("a",{attrs:{href:"https://vuex.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vuex")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-devtools#vue-devtools",target:"_blank",rel:"noopener"}},[t._v("vue-devtools")])]),a("li",[a("a",{attrs:{href:"https://vue-loader.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vue-loader")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/awesome-vue",target:"_blank",rel:"noopener"}},[t._v("awesome-vue")])])])}],B={name:"HelloWorld",props:{msg:String}},j=B,L=(a("c1c7"),Object(g["a"])(j,x,N,!1,null,"25d525f8",null)),w=L.exports,M={name:"Home",components:{HelloWorld:w}},P=M,U=Object(g["a"])(P,k,D,!1,null,null,null),F=U.exports,H=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},[t._v(" "+t._s(t.msg)+" ")])},Y=[],G={name:"Ping",data:function(){return{msg:""}},methods:{getMessage:function(){var t=this,e="http://localhost:5000/ping";m.a.get(e).then((function(e){t.msg=e.data})).catch((function(t){console.error(t)}))}},created:function(){this.getMessage()}},$=G,q=Object(g["a"])($,H,Y,!1,null,null,null),X=q.exports;r["a"].use(R["a"]);var W=[{path:"/",name:"Home",component:F},{path:"/ping",name:"Ping",component:X},{path:"/about",name:"About",component:function(){return a.e("about").then(a.bind(null,"f820"))}}],z=new R["a"]({mode:"history",base:"/",routes:W}),V=z;r["a"].config.productionTip=!1,new r["a"]({router:V,render:function(t){return t(I)}}).$mount("#app")},"7d33":function(t,e,a){t.exports=a.p+"img/SMF_A_plain@3x.76fb46f1.png"},"85ec":function(t,e,a){},8940:function(t,e,a){},"99ad":function(t,e,a){t.exports=a.p+"img/hugo_dolan_analytics.e52edd8b.png"},a324:function(t,e,a){},c1c7:function(t,e,a){"use strict";a("fe5e")},cf05:function(t,e,a){t.exports=a.p+"img/logo.82b9c7a5.png"},f968:function(t,e,a){"use strict";a("a324")},fe5e:function(t,e,a){}});
//# sourceMappingURL=app.dbb4448a.js.map