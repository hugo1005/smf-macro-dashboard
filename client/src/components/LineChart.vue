<!-- 
Good example here bar chart ---[ https://stackoverflow.com/questions/48726636/draw-d3-axis-without-direct-dom-manipulation 
-->

<template>
    <div v-if="!loading">
        <h1><span v-bind:style={color:highlight[category]}>{{getShortendedCategory(category)}}</span>{{title}} <span class='float-right' v-if="show_pct" :style="{color: getAttributionColor(getPctChange())}">[{{getPctChange()}} %]</span></h1>
        <svg :width="chartDefaults.width + chartDefaults.margin.left + chartDefaults.margin.right" :height="chartDefaults.height + chartDefaults.margin.top + chartDefaults.margin.bottom" v-bind:style="{
            'background-image': 'linear-gradient(' + background[category] + '00,' + background[category] + ')'
            }">

            <g class='lineChart' v-bind:transform="translate">
            
            <axis class='yA' v-bind:scales="getScales().yAxis" v-bind:chartDefaults='chartDefaults' v-bind:data='data' v-bind:trns='trnsY'/>
            
            <axis class='xA' v-bind:scales="getScales().xAxis" v-bind:chartDefaults='chartDefaults' v-bind:data='data' v-bind:trns='trnsX()'/>
            
            <!-- <axis class='grid' v-bind:scales="getScales().yGrid" v-bind:chartDefaults='chartDefaults' v-bind:data='data' v-bind:trns='trnsY' v-bind:style="{opacity: chartDefaults.gridOpacity}"/> -->
            
            <path class='line' :d="line"/>
            <circle 
            :cx="getScales().x(data[this.data.length - 1].date)" 
            :cy='getScales().y(data[this.data.length - 1].value)' 
            r='3' fill='#fff'>
                  
            </circle>
            <text 
            :x="getScales().x(data[this.data.length - 1].date)" 
            :y="getScales().y(data[this.data.length - 1].value)"
            :fill='highlight[category]'
            dx="-10"
            dy='-10'
            style='font-size: 10px;'
            >{{roundData(data[this.data.length - 1].value,2)}}</text>  
            
            </g>
            
        </svg>
        
    </div>
</template>

<script>
import * as d3 from "d3";
import Axis from "../components/Axis.vue";
import axios from 'axios';
import {round} from 'mathjs';

export default {
    name: "vue-line-chart",
    components: {
        axis: Axis // Using reusable component to draw x,y axis and Grid.
    },
    props: ['title', 'data','category', 'background','highlight','month_tick_interval', 'show_pct','short_category'],
    data() {
        return {
        loading: true,
        chartDefaults: {
            width: 160,
            height: 100,
            chartId: "linechart-vue",
            margin: {
                top: 5,
                right: 0,
                bottom: 30,
                left: 50
            },
            gridOpacity: 1,
            data: []
        },
        line: "",
        //Translate co-ords for chart, x axis and yaxis. This is injected into template
        translate: "translate(" + 35 + "," + 5 + ")",
        trnsY: "translate(0,0)",
        trnsX: this.getTrnsx,
        toggleClass: true
        };
    }, 
    created() {
        this.calculatePath();
        this.loading = false
    },
    methods: {
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
        getPctChange() {
            let last = this.data[this.data.length - 1].value
            let first = this.data[0].value
            let pct = (( last / first) - 1) * 100
            return this.roundData(pct, 2)
        },
        getScales() {
            console.log("Drawing scales...")
            console.log(this.data[0].date)
            // All the maths to work chart co ordinates and woring out Axis

            const y_extent = d3.extent(this.data, d => d.value);

            const x = d3
                .scaleTime()
                .domain(
                    d3.extent(this.data, function(d) {
                        return d.date;
                    })
                )
                .rangeRound([0, this.chartDefaults.width - this.chartDefaults.width * 0]);
            const y = d3
                .scaleLinear()
                .domain([y_extent[0] - (y_extent[1]-y_extent[0])*0.2, y_extent[1] + (y_extent[1]-y_extent[0])*0.2])
                .range([this.chartDefaults.height, 0]);

            d3.axisBottom().scale(x);
            d3.axisLeft().scale(y);

            //Key funtions to draw X-axis,YAxis and the grid. All uses component axis
            //play around with time format to get it to display as you want : d3.timeFormat("%b-%d")
            var xAxis = d3
                .axisBottom()
                .scale(x)
                .ticks(d3.timeMonth.every(this.month_tick_interval))
                .tickFormat(d3.timeFormat('%b-%y'));

            var yAxis = d3
                .axisLeft()
                .scale(y)
                .ticks(5);
                
            var yGrid = d3
                .axisLeft()
                .scale(y)
                .tickSize(-(this.chartDefaults.width - 100), 0, 0)
                .tickFormat("");

            // Return the key calculations and functions to draw the chart
            return {
                x,
                y,
                xAxis,
                yAxis,
                yGrid
            };
        },
        getTrnsx(chartDefaults) {
        //works out translate value in realtive to dynamic height
        const t = "translate(0," + this.chartDefaults.height + ")";
        return t;
        },
        calculatePath() {
            console.log("Drawing path")
            //Get key calculation funtions to draw chart , Ie scale, axis mapping and plotting
            const scale = this.getScales();
            // Define calcultion to draw chart
            const path = d3
                .line()
                .x(d => {
                    return scale.x(d.date);
                })
                .y(d => {
                    return scale.y(d.value);
                })

            // draw line then this.line is injected into the template
            this.line = path(this.data);
        }
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
