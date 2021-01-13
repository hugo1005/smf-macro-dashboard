<template>
  <div id="app">
    <div id='banner' class='padded'>
      <img src='./assets/SMF_A_plain@3x.png'>   
      <img src='./assets/hugo_dolan_analytics.png'>        
    </div>
    <div class="macro-bg">
      <div id='chart-header'>
          <h1>
          Macro Overview
          </h1>
      </div> 
      <div v-if="!loading" id='chart-container'>
        
        <div v-for="key in Object.keys(data)" :key="key">
          <LineChart class='chart' v-bind:category='key.split("_")[0]' v-bind:title='key.split("_").slice(1,).join(" ")' v-bind:data='data[key]' :background="background_macro" :highlight="highlight_macro" :month_tick_interval="4"></LineChart>
        </div>
      </div>
    </div>

    <div class='macro-bg'>
      <div id='chart-header'>
        <h1>
          Risk Dashboard  
        </h1> 
      </div>

      <div v-if="!loading_risk"  class='padded'>
        <div id='port-stats'>
            <h2>PORTFOLIO STATISTICS</h2>
            <div id='port-stats-data'>
              <div class='port-stat'>
                <div class='port-stat-name'>RETURN</div>
                <div class='port-stat-value'>{{risk.attribution.regions.Overall['Portfolio Total Return']}} %</div>
              </div>
              <div class='port-stat'>
                <div class='port-stat-name'>EXCESS RETURN</div>
                <div class='port-stat-value'>{{risk.attribution.regions.Overall['Total Effect']}} %</div>
              </div>
              <div class='port-stat'>
                <div class='port-stat-name'>EUROPE WEIGHT</div>
                <div class='port-stat-value'>{{roundToTwo(risk.weightings.region_weights.EU * 100)}} %</div>
              </div>
              <div class='port-stat'>
                <div class='port-stat-name'>US WEIGHT</div>
                <div class='port-stat-value'>{{roundToTwo(risk.weightings.region_weights.US * 100)}} %</div>
              </div>
              <div class='port-stat'>
                <div class='port-stat-name'>ALPHA</div>
                <div class='port-stat-value'>{{risk.portfolio_summary_stats.alpha}}</div>
              </div>
              <div class='port-stat'>
                <div class='port-stat-name'>BETA</div>
                <div class='port-stat-value'>{{risk.portfolio_summary_stats.beta}}</div>
              </div>
              <div class='port-stat'>
                <div class='port-stat-name'>SHARPE</div>
                <div class='port-stat-value'>{{risk.portfolio_summary_stats.sharpe}}</div>
              </div>
              <div class='port-stat'>
                <div class='port-stat-name'>TRACKING ERROR</div>
                <div class='port-stat-value'>{{risk.portfolio_summary_stats.tracking_error_pct}} %</div>
              </div>
            </div>
          </div>
        <div class='dash-panel'>
          

          <div id='port-attribution-panel'>
            <h2>RETURN ATTRIBUTION OVERVIEW</h2>
            <div id='attr-data'>
              <div class='attr-stat'>
                <h3 class='attr-stat-head'>
                  <span style="color:#FF1414;"><br></span><br>
                  <span style="color:#ffffff90;"></span></h3>
                <div class='attr-stat-box-label' v-for="effect in effects" :key='effect'>
                  <svg width='100%' height='100%'>
                    <rect width='100%' height="100%" fill='#A84E4E70'></rect>
                    <!-- <circle :r="getPctAttributionRadius(r_data[effect])" :fill="getAttributionColor(r_data[effect])" cx='50%' cy='50%'></circle> -->
                    <text fill='#FF1414' font-size="14" text-anchor='middle' transform="translate(20,60) rotate(270 0 0)">{{effects_map[effect]}}</text>
                  </svg>
                </div>
              </div>
              <div class='attr-stat border-left' v-for="[region, r_data] in regions.map(r => [r, risk.attribution.regions[r]])" :key="region">
                <h3 class='attr-stat-head'>
                  <span style="color:#92cbf1;">{{r_data['Benchmark Total Return']}}% RETURN</span><br>
                  <span style="color:#ffffff90;">{{regions_short[region]}} INDEX</span>
                </h3>
                <div class='attr-stat-box' v-for="effect in effects" :key='effect'>
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
                    <circle :r="getPctAttributionRadius(r_data[effect], risk.attribution.regions)" :fill="getAttributionGrad(r_data[effect])" cx='50%' cy='50%'></circle>
                    <text x='4%' y='96%' fill='#ffffff90' text-anchor='right' dominant-baseline='top'>{{r_data[effect]}}%</text>
                  </svg>
                </div>
                <h3 class='attr-stat-head'>
                  <span :style="{color:getAttributionColor(r_data['Portfolio Total Return'])}">{{r_data['Portfolio Total Return']}}% RETURN</span><br>
                  <span style="color:#fff">{{regions_short[region]}} PORTFOLIO</span>
                </h3>
              </div>
            </div>
          </div>  

          <div id='port-attribution-panel'>
            <h2>PORTFOLIO WEIGHTING BREAKDOWN</h2>
            <tree-chart id='port-sector-weights' v-bind:data='risk.weightings' :background="background_equities" :highlight="highlight_equities" :short_category="short_equities"></tree-chart>
          </div>
        </div>
        

        <div class="macro-bg">
          <h2>Equity Charts</h2>
          <div v-if="!loading_risk" id='chart-container'>
            
            <div v-for="key in Object.keys(risk.equities)" :key="key">
              <LineChart class='chart' v-bind:category='key.split("_")[0]' v-bind:title='key.split("_").slice(1,).join(" ")' v-bind:data='risk.equities[key]' :background="background_equities" :highlight="highlight_equities" :month_tick_interval="1" :show_pct="true" :short_category="short_equities"></LineChart>
            </div>
          </div>
        </div>

        <!-- <div class="macro-bg">
          <h2>CORRELATIONS PORT V BENCHMARK</h2>
          <correlation-plot :data='risk.correlations.portfolio_v_port' :short_category="sectors_short"></correlation-plot>
        </div> -->

        <div id='port-attribution-panel' v-for="[region, r_data] in Object.entries(risk.attribution.sectors)" :key="region">
            <h2>{{regions_short[region]}} SECTOR ATTRIBUTION SCORING</h2>
            <div id='attr-data'>
              <div class='attr-stat'>
                <h3 class='attr-stat-head'>
                  <span style="color:#FF1414;"><br></span><br>
                  <span style="color:#ffffff90;"></span></h3>
                <div class='attr-stat-box-label' v-for="effect in effects" :key='effect'>
                  <svg width='100%' height='100%'>
                    <rect width='100%' height="100%" fill='#A84E4E70'></rect>
                    <!-- <circle :r="getPctAttributionRadius(r_data[effect])" :fill="getAttributionColor(r_data[effect])" cx='50%' cy='50%'></circle> -->
                    <text fill='#FF1414' font-size="14" text-anchor='middle' transform="translate(20,60) rotate(270 0 0)">{{effects_map[effect]}}</text>
                  </svg>
                </div>
              </div>
              <div class='attr-stat border-left' v-for="[sector, s_data] in Object.entries(r_data)" :key="sector">
                <h3 class='attr-stat-head'>
                  <span style="color:#92cbf1;">{{s_data['Benchmark Total Return']}}% RETURN</span><br>
                  <span style="color:#ffffff90;">{{sectors_short[sector]}} INDEX</span>
                </h3>
                <div class='attr-stat-box' v-for="effect in effects" :key='effect'>
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
                    <circle :r="getPctAttributionRadius(s_data[effect], r_data)" :fill="getAttributionGrad(s_data[effect])" cx='50%' cy='50%'></circle>
                    <text x='4%' y='96%' fill='#ffffff90' text-anchor='right' dominant-baseline='top'>{{s_data[effect]}}%</text>
                  </svg>
                </div>
                <h3 class='attr-stat-head'>
                  <span :style="{color:getAttributionColor(s_data['Portfolio Total Return'])}">{{s_data['Portfolio Total Return']}}% RETURN</span><br>
                  <span style="color:#fff">{{sectors_short[sector]}} PORTFOLIO</span>
                </h3>
              </div>
            </div>
          </div> 
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from "./components/LineChart.vue";
import TreeChart from "./components/TreeChart.vue";
import CorrelationPlot from "./components/CorrelationPlot.vue";
import axios from 'axios';
import * as d3 from "d3";

export default {
  name: "App",
  components: {
    LineChart,
    TreeChart,
    CorrelationPlot
  },
  data() {
    return {
      data: {},
      loading: true,
      risk: {},
      loading_risk: true,
      effects: ['Selection Effect','Allocation Effect','Total Effect'],
      effects_map: {'Selection Effect':'Selection Effect','Allocation Effect':'Allocation Effect','Total Effect':'Outperformance'},
      regions: ['Overall','US','Europe'],
      regions_short: {'Overall': 'OVERALL','US': 'US','Europe':'EU'},
      sectors_short: {"Communications": "COMMS",
        "Consumer_Disrectionary": "DISC.",
        "Consumer_Staples": "STAPLES",
        "Energy_Renewables": "ENERGY",
        "Financials": "FINANCIALS",
        "Health_Care": "HEALTH",
        "Information_Technology": "TECH",
        "Industrials": "INDUSTRY",
        "Utilities": "UTILITIES",
        "Other": "OTHER"},
        background_macro: {
            BOND:"#AD3B3B",
            "FX|COMMODITY":"#86AD3B",
            INDEX:"#3BA9AD",
            METRIC:"#743BAD",
            COMMODITITY:"#AD3BA0",
            SURVEY:"#3B51AD"
        },
        highlight_macro: {
            BOND:"#E55151",
            "FX|COMMODITY":"#A7D64B",
            INDEX:"#4CCED3",
            METRIC:"#B47CEB",
            COMMODITITY:"#AD3BA0",
            SURVEY:"#6B84EB"
        },
        highlight_equities: {
          "COMMUNICATIONS": "#E55151",
          "CONSUMER DISRECTIONARY": "#A7D64B",
          "CONSUMER STAPLES": "#4CCED3",
          "ENERGY RENEWABLES": "#B47CEB",
          "FINANCIALS": "#AD3BA0",
          "HEALTH CARE": "#6B84EB",

          "INFORMATION TECHNOLOGY": "#E5AC51",
          "INDUSTRIALS": "#4BD6A6",
          "UTILITIES": "#EFADEF",
          "OTHER": "#B47CEB"
        },
        background_equities: {
          "COMMUNICATIONS": "#AD3B3B",
          "CONSUMER DISRECTIONARY": "#86AD3B",
          "CONSUMER STAPLES": "#3BA9AD",
          "ENERGY RENEWABLES": "#743BAD",
          "FINANCIALS": "#AD3BA0",
          "HEALTH CARE": "#3B51AD",

          "INFORMATION TECHNOLOGY": "#AD8A3B",
          "INDUSTRIALS": "#3BAD70",
          "UTILITIES": "#C904AB",
          "OTHER": "#743BAD"
        },
        short_equities: {
          "COMMUNICATIONS": "COMMS",
          "CONSUMER DISRECTIONARY": "DISC.",
          "CONSUMER STAPLES": "STAPLES",
          "ENERGY RENEWABLES": "ENERGY",
          "FINANCIALS": "FINANCIALS",
          "HEALTH CARE": "HEALTHCARE",

          "INFORMATION TECHNOLOGY": "TECH",
          "INDUSTRIALS": "INDUSTRIALS",
          "UTILITIES": "UTILITIES",
          "OTHER": "OTHER"
        },
    }
  },
  methods: {
    roundToTwo: function(num) {    
      return +(Math.round(num + "e+2")  + "e-2");
    },
    getPctAttributionRadius: function(r_unscaled, regions_data) {
        // Gets the maximum value for the region
        // This will be equivalent to 50% radius
        // this.risk.attribution.regions
        let region_values = Object.values(regions_data)
        
        let vals = region_values.map(y => this.effects.map(key => y[key])).flat()
        let max_val = Math.max(...vals)
        
        let relative_size = r_unscaled / max_val
        return Math.abs(relative_size * 30) + "%"
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
  },
  created() {
        
        let path_chart = './chart_data'
        
        if(process.env.NODE_ENV === 'development') {
          path_chart = 'http://localhost:5000/chart_data';
        }
        
        axios.get(path_chart)
            .then((res) => {
                console.log("Recieved data...")
                this.data = res.data

                var parseDate = d3.timeParse("%Y-%m-%d");

                Object.keys(this.data).forEach((key) => {
                  this.data[key].forEach(function(d) {
                    d.date = parseDate(d.date);
                  });
                });
                
                console.log("Recieved data...")
                this.loading = false
            })
            .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
            }); 

        
        let path_risk = './risk_data'

        if(process.env.NODE_ENV === 'development') {
          path_risk = 'http://localhost:5000/risk_data';
        }
        axios.get(path_risk)
            .then((res) => {
                console.log("Recieved data...")
                this.risk = res.data

                var parseDate = d3.timeParse("%Y-%m-%d");

                Object.keys(this.risk.equities).forEach((key) => {
                  this.risk.equities[key].forEach(function(d) {
                    d.date = parseDate(d.date);
                  });
                });

                this.loading_risk = false
            })
            .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
            }); 
    },
};
</script>

<style>
  body {
    background-color: #f7f7f7; 
    padding: 0;
    padding-bottom: 60px;
    margin: 0;
    background-image: linear-gradient(#380404,#380404);
  }

  h1 {
      color: white;
      font-family: Roboto;
      font-size: 10px;
      text-align: left;
      padding-left: 10px;
      padding-bottom: 5px;
      padding-top: 5px;
      margin-top:0px;
      margin-bottom: 0px;
      background: none;
  }

  #banner {
      position: fixed;
      bottom:0;
      background: #1e0204db;
      width: 100%;
      height: 65px;
      /* border-bottom: 6px solid #fc6368; */
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      
  }

  .padded {
      padding: 16px;
      box-sizing: border-box;
  }

  #banner img {
      height: 30px;
      margin: 0 2%;
  }


  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #chart-header {
      align-self: right;
  }

  #chart-header h1 {
      color: white;
      font-family: Roboto;
      font-size: 30px;
      text-align: left;
      background: rgba(4, 0, 1, 0.247);
      width: 100%;
      margin: 10px auto;
      margin-bottom: 0px;
      padding: 20px 30px;
  }

  #chart-container {
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      align-content: center;
      justify-content: center;
  }

  .chart {
    margin: 8px;
  }

  table {
      width: 100%;
      text-align: center;
      font-family: 'Libre Baskerville', serif;
      font-size: 9pt;
      border-spacing: 0;
  }

  table th {
      font-weight: 700;
      border-top: 2px solid #333334;
      border-bottom: 2px solid #333334;
      padding-top: 8px;
      padding-bottom: 8px;
  }

  table td {
      font-weight: 400;
      padding-bottom: 4px;
      padding-top: 4px;
  }

  table tr:nth-child(even) {
      background-color: #f2f2f2;
  }

  .macro-bg {
    background-image: url("./assets/bg_low_alpha.png");
    background-size: fit;
  }

  .dash-panel {
    display: flex;
    width: 100%;
    flex-direction: row;
  }

  #port-attribution-panel {
    max-width: 100%;
    margin-bottom: 20px;
  }

  #attr-data {
    width: 100%;
    display: flex;
    flex-direction: row;
    padding: 10px 20px;
  }

  .attr-stat {
    display: flex;
    flex-direction: column;

  }

  .border-left {
    margin-right: 8px;
    /* border-right: 2px solid #A84E4E30; */
  }

  .attr-stat-box-label {
    width: 30px;
    height: 120px;
    font-family: 'Roboto', sans-serif;
    font-weight: 300;
    margin: 9px 8px;
    display: flex;
    flex-direction: column;
    align-content: center;
    justify-content: center;
  }

  .attr-stat-box {
    width: 120px;
    height: 120px;
    font-family: 'Roboto', sans-serif;
    color: white;
    font-weight: 300;
    border: 1px solid #ffffff30;
    margin: 8px;
    display: flex;
    flex-direction: column;
    align-content: center;
    justify-content: center;
  }

  .attr-stat-head {
    font-family: 'Roboto', sans-serif;
    color: white;
    font-size: 12px;
    text-align: left;
    margin: 4px 12px;
  }

  #port-stats {
    width: 100%;
    background-image: linear-gradient(#0A174F30,#0d1d5f50);
    padding: 0 10px;
    box-sizing: border-box;
  }

  h2 {
    font-family: 'Roboto', sans-serif;
    font-size: 18px;
    color: #92cbf1;
    padding: 16px;
    margin-top: 0px;
    text-align: left;
    border-bottom: 1px solid rgb(13, 86, 170);
    margin-bottom: 5px;
  }

  #port-stats-data {
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding-bottom: 16px;
    box-sizing: border-box;
  }

  .port-stat {
    font-family: 'Roboto', sans-serif;;
    width: 90%;
    background: #A84E4E70;
    display: flex;
    padding: 8px 8px;
    font-size: 10px;
    box-sizing: border-box;
    flex-direction: row;
    justify-content: space-between;
    margin: 0px 4px;
  }

  .port-stat-name {
    color: #FF1414;
    font-weight: 700;
  }

  .port-stat-value {
    color: white;
    font-weight: 300;
  }
</style>
