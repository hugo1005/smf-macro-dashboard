<!-- 
Good example here bar chart ---[ https://stackoverflow.com/questions/48726636/draw-d3-axis-without-direct-dom-manipulation 
-->

<template>
    <div v-if="!loading" class='corr-flex-col'>
        <div class='corr-header corr-flex-row'>
            <div  v-for="c_cat in col_cats" :key="'col_' + c_cat" class='corr-header-container'>
                <div class='corr-label'> 
                    {{getShortendedCategory(c_cat)}} <br><div style='opacity: 40%;'>[BENCH]</div>
                </div>
            </div>
        </div>
        <div class='corr-flex-row'>
            <div class='corr-flex-col'>
                <div v-for="r_cat in row_cats" :key="'row_' + r_cat" class='corr-label-container'>
                    <div class='corr-label'>
                        {{getShortendedCategory(r_cat)}} <br><div style='opacity: 40%;'>[PORT]</div>
                    </div>
                </div>
            </div>
            
            <div  class='corr-flex-row' v-for="[cat_col, col_data] in Object.entries(data)" :key="cat_col">
                <div class='corr-flex-col'>
                    <div class='corr-stat-box' v-for="[cat_row, value] in Object.entries(col_data)" :key="cat_row">
                        
                        <svg width='100%' height='100%'>
                            <defs>
                                <linearGradient id="gradPos" x1="0%" y1="0%" x2="0%" y2="100%">
                                <stop offset="0%" style="stop-color:#86AD3B;stop-opacity:1" />
                                <stop offset="100%" style="stop-color:#A7D64B;stop-opacity:0.3" />
                                </linearGradient>
                                <linearGradient id="gradNeg" x1="0%" y1="0%" x2="0%" y2="100%">
                                <stop offset="0%" style="stop-color:#AD3B3B;stop-opacity:1" />
                                <stop offset="100%" style="stop-color:#E55151;stop-opacity:0.3" />
                                </linearGradient>
                            </defs>
                            <circle :r="getPctAttributionRadius(value, true)" :fill="getAttributionColor(value) + '40'" cx='50%' cy='50%'></circle>
                            <text x='50%' y='50%' :fill='getAttributionColor(value)' text-anchor='middle' :font-size='getPctAttributionRadius(value, false)' dominant-baseline='middle'>{{value}}</text>
                        </svg>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import * as d3 from "d3";
import axios from 'axios';
import {round, sum} from 'mathjs';

export default {
    name: "vue-correlation-plot",
    props: ['data','short_category'],
    data() {
        return {
            max_radius: 0,
            col_cats: [],
            row_cats: [],
            loading: true,
        };
    }, 
    created() {
        this.max_radius = 1
        this.col_cats = Object.keys(this.data)
        this.row_cats = Object.keys(this.data[this.col_cats[0]])
        this.loading = false
    },
    methods: {
        getShortendedCategory: function(cat) { 
            let split_cat = cat.split('_').slice(0,cat.split('_').length - 1).join('_')
            
            if(this.short_category) {
                return this.short_category[split_cat]
            } else {
                return split_cat
            }
            
        },
        roundData(d, digits) {
            return round(d, digits)
        },
        getPctAttributionRadius: function(r_unscaled, circle) {
            // Gets the maximum value for the region
            // This will be equivalent to 50% radius
            // this.risk.attribution.regions
            let relative_size =  r_unscaled / this.max_radius 
            if(circle) {
                return Math.abs(relative_size * 30) + "%"
            } else {
                return Math.abs(relative_size * 20) + "px"
            }
            
        },
        getAttributionGrad: function(r_unscaled) {
            if(r_unscaled >= 0) {
                return 'url(#gradPos)'
            } else {
                return 'url(#gradNeg)'
            }
        },
        getAttributionColor: function(r_unscaled) {
            if(r_unscaled >= 0) {
                return '#86AD3B'
            } else {
                return '#AD3B3B'
            }
        }
    }
};
</script>
<!-- css loaderhttps://vue-loader.vuejs.org/guide/scoped-css.html#mixing-local-and-global-styles -->
<style>
    .corr-stat-box {
        width: 50px;
        height: 50px;
        font-family: 'Roboto', sans-serif;
        color: white;
        font-weight: 300;
        border: 1px solid #ffffff20;
        margin: 4px;
        display: flex;
        flex-direction: column;
        align-content: center;
        justify-content: center;
    }

    .corr-flex-col {
        display:flex;
        flex-direction: column;
    }

    .corr-flex-row {
        display:flex;
        flex-direction: row;
    }

    .row-labels {
        height: 50px;
    }

    .corr-label {
        font-family: 'Roboto', sans-serif;
        color:#ffffff90;
        font-size: 10px;
    }

    .corr-label-container {
        height: 52px;
        margin: 4px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .corr-header-container {
        width: 52px;
        margin: 4px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .corr-header {
        margin-left: 63px;
    }
</style>
