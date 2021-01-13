<template>
  <g :transform='trns'>
        <g ref="axis"  >
        </g>
    </g>
</template>

<script>
import * as d3 from "d3";
export default {
  name: "axis",
  props: {
    scales: Function,
    chartDefaults: Object,
    data: Array,
    trns: String
  },

  data() {
    return {
      width: 0,
      height: 0
    };
  },
  mounted() {
    var node = this.$refs.axis;

    // d3.select(node).call(this.scales());
    d3.select(node).call(this.scales);
  }
};
</script>

<style>
.yA path,
.grid path,
.yA .tick line {
  stroke: transparent;
}
</style>
