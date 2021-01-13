<!-- 
Good example here bar chart ---[ https://stackoverflow.com/questions/48726636/draw-d3-axis-without-direct-dom-manipulation 
-->

<template>
    <div v-if="!loading">
        <!-- <h1><span v-bind:style={color:highlight[category]}>{{getShortendedCategory(category)}}</span>{{title}} <span class='float-right' v-if="show_pct" :style="{color: getAttributionColor(getPctChange())}">[{{getPctChange()}} %]</span></h1> -->
        <svg :width="chartDefaults.width + chartDefaults.margin.left + chartDefaults.margin.right" :height="chartDefaults.height + chartDefaults.margin.top + chartDefaults.margin.bottom">
        <g v-for="s_child in root.children" :key="s_child.data.name">
            <defs>
            <linearGradient :id="s_child.data.name.replace(' ','-')" gradientTransform="rotate(90)">
            <stop offset="0%" :stop-color="background[s_child.data.name]+'60'"/>
            <stop offset="100%" :stop-color="background[s_child.data.name]"/>
            </linearGradient>
            <linearGradient :id="s_child.data.name.replace(' ','-')+'-h'" gradientTransform="rotate(90)">
            <stop offset="0%" :stop-color="highlight[s_child.data.name]+'60'"/>
            <stop offset="100%" :stop-color="highlight[s_child.data.name]"/>
            </linearGradient>
            </defs>
            <!--   -->

            <rect v-if="s_child.data.port_sector_weight > 0"
                :x="s_child.x0" 
                :y="s_child.y0" 
                :width="s_child.x1 - s_child.x0" 
                :height="s_child.y1 - s_child.y0"
                :fill="background[s_child.data.name]+'30'"
                >
            </rect>
            
            <g v-for="r_child in s_child.children" :key="r_child.data.name + s_child.data.name">
                

                <g v-if="r_child.data.port_weight > 0">
                    <rect
                    :x="r_child.x0" 
                    :y="r_child.y0" 
                    :width="r_child.x1 - r_child.x0" 
                    :height="r_child.y1 - r_child.y0"
                    :style="getFillStyle(s_child.data.name,r_child.data.name)" 
                    >
                    </rect>

                    <g v-for="e_child in r_child.children" :key="e_child.data.name">
                        <rect
                        :x="e_child.x0" 
                        :y="e_child.y0" 
                        :width="(e_child.x1 - e_child.x0)" 
                        :height="e_child.y1 - e_child.y0"
                        stroke='#ffffff30'
                        fill=none
                        >
                        </rect>

                        <text 
                        :x="e_child.x0 + 5" 
                        :y="e_child.y0 + 10" 
                        font-size="10"
                        text-anchor='left'
                        dominant-baseline='middle'
                        fill='#ffffff30' 
                        >
                        {{e_child.data.name}}
                        </text>

                        <text 
                        :x="e_child.x1 - 5" 
                        :y="e_child.y1 - 10" 
                        font-size="10"
                        text-anchor='end'
                        dominant-baseline='middle'
                        fill='#ffffff30' 
                        >
                        {{roundData(e_child.data.port_weight * 100,2)}} % 
                        </text>
                    </g>

                    <text 
                        text-anchor='left' 
                        dominant-baseline='middle' 
                        :x="r_child.x0 + 5" 
                        :y="r_child.y0 + 10" 
                        fill='#ffffff80'  
                        font-size="10">
                        {{r_child.data.name}} ({{roundData(r_child.data.port_weight * 100,2)}} %)
                    </text>
                </g>
                
            </g>
            <text v-if="s_child.data.port_sector_weight > 0"
                :x="s_child.x0 + chartDefaults.padding.outer + 5" 
                :y="s_child.y0 + chartDefaults.padding.top/2" 
                :fill='highlight[s_child.data.name]' 
                font-size="10"
                dominant-baseline='middle'
            >
                {{getShortendedCategory(s_child.data.name)}} ({{roundData(s_child.data.port_sector_weight * 100,2)}} %)
            </text>

            <text v-if="s_child.data.port_sector_weight > 0"
                text-anchor='end' 
                dominant-baseline='middle' 
                :x="s_child.x1 - 5" 
                :y="s_child.y0 + 10" 
                :fill='getAttributionColor(s_child.data.benchmark_deviation)'  
                font-size="10">
                [{{roundData((s_child.data.benchmark_deviation) * 100,2)}} %]
            </text>
        </g>
        </svg>
    </div>
</template>

<script>
import * as d3 from "d3";
import axios from 'axios';
import {round, sum} from 'mathjs';

export default {
    name: "vue-tree-chart",
    props: ['data','background','highlight','short_category'],
    data() {
        return {
            loading: true,
            root: {},
            chartDefaults: {
                width: 800,
                height: 550,
                chartId: "linechart-vue",
                margin: {
                    top: 0,
                    right: 0,
                    bottom: 0,
                    left: 0
                },
                gridOpacity: 1,
                data: [],
                padding: {
                    inner: 0,
                    outer: 2,
                    top:20,
                    bottom:0
                }
            },
            line: "",
            //Translate co-ords for chart, x axis and yaxis. This is injected into template
            trnsY: "translate(0,0)",
            trnsX: this.getTrnsx,
        };
    }, 
    created() {
        this.translate = "translate(" + this.chartDefaults.margin.left + "," + this.chartDefaults.margin.top + ")";
        this.calculateTree();
        this.loading = false
    },
    methods: {
        calculateTree: function() {
            this.root = d3.hierarchy(this.data).sum(function(d){ return d.port_weight}) 
            d3.treemap().tile(d3.treemapBinary).size([this.chartDefaults.width,this.chartDefaults.height]).paddingInner(this.chartDefaults.padding.inner)
            .paddingOuter(this.chartDefaults.padding.outer).paddingTop(this.chartDefaults.padding.top).paddingBottom(this.chartDefaults.padding.bottom)(this.root);
        },
        getShortendedCategory: function(cat) { 
            if(this.short_category) {
                return this.short_category[cat]
            } else {
                return cat
            }
            
        },
        getAttributionColor: function(r_unscaled) {
            if(r_unscaled >= 0) {
                return '#86AD3B'
            } else {
                return '#AD3B3B'
            }
        },
        roundData(d, digits) {
            return round(d, digits)
        },
        getFillStyle(s_name, r_name) {
            return r_name == 'EU'? {fill:'url(#'+s_name.replace(' ','-')+'-h)'}: {fill:'url(#'+s_name.replace(' ','-') + ')'}
        },
    }
};
</script>
<!-- css loaderhttps://vue-loader.vuejs.org/guide/scoped-css.html#mixing-local-and-global-styles -->
<style>
h1 {
    color: white;
    font-family: Roboto;
    font-size: 10px;
    text-align: left;
    padding-left: 10px;
    padding-bottom: 5px;
    padding-top: 5px;
    margin-top:0px;
    background: #b23d3d30;
}

h1 span {
    margin-right: 10px;
}

path.line {
  fill: none;
  stroke: white;
  stroke-width: 1px;
}

.grid line {
  opacity: 0.05;
  color:white;
}
.xA line {
  opacity: 0.5;
}

.xA {
    color:white;
}

.yA {
    color:white;
}

/*Some fancy animation to draw chart*/
/* svg .lineChart > path {
  stroke: #ecbc3a;
  stroke-width: 3;
  stroke-dasharray: 4813.713;
  stroke-dashoffset: 4813.713;
}

.ani2 svg .lineChart > path {
  stroke: #ecbc3a;
}
.ani1 svg .lineChart > path {
  stroke: #ecbc3a;
} */

#Layer_1 {
  width: 100%;
}

.text {
  display: inline-block;
  font-size: 3vw;
  margin: 0.5vw 0 1.5vw;
}

svg {
  border-bottom: 1px solid rgba(256,256,256,0.1);
  margin-bottom: 0;
}

.float-right {
    float: right;
}
</style>
