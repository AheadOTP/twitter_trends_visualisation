<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld :msg="chartData"/> -->
    <Form @parentSearch="loadTweets"/>
    <fingerprint-spinner
      id="loader"
      :animation-duration="1500"
      :size="64"
      color="#ff1d5e"
      v-bind:class="{ invisible: !isLoading }"
    />
    <GChart
      type="ColumnChart"
      :data="chartData"
      :options="columnChartOptions"
      :events="columnChartEvents"
      ref="gColumnChart"
    />
    <GChart
      type="PieChart"
      :data="chartData"
      :options="pieChartOptions"
      :events="pieChartEvents"
      ref="gPieChart"
    />
    <VisibleTweets
      :text="visibleTweets"
    />
  </div>
</template>

<script>
import TweetService from './TweetService'
// import HelloWorld from './components/HelloWorld.vue'
import Form from './components/Form.vue'
import VisibleTweets from './components/VisibleTweets.vue'
import { GChart } from 'vue-google-charts'
import { FingerprintSpinner } from 'epic-spinners'

export default {
  name: 'app',
  components: {
    // HelloWorld,
    Form,
    VisibleTweets,
    GChart,
    FingerprintSpinner
  },
  data(){
    return{
        chartData: [],
        columnChartOptions: {
          chart: {
            title: 'Popular topics',
            subtitle: 'Tweets count',
          }
        },
        pieChartOptions: {
          title: 'Popular topics',
          is3D: true
        },
        columnChartEvents: {
          select: () => {          
            const table = this.$refs.gColumnChart.chartObject;
            const selection = table.getSelection();          
            console.log(this.chartData[selection[0].row + 1][0])
            this.visibleTweets = this.tweetsForTopics[this.chartData[selection[0].row + 1][0]]
            console.log("visible tweets: ", this.visibleTweets)
            // const onSelectionMeaasge = selection.length !== 0 ? 'row was selected' : 'row was diselected'
            // alert(onSelectionMeaasge);
          }
        },
        pieChartEvents: {
          select: () => {          
            const table = this.$refs.gPieChart.chartObject;
            const selection = table.getSelection();          
            console.log(this.chartData[selection[0].row + 1][0])
            this.visibleTweets = this.tweetsForTopics[this.chartData[selection[0].row + 1][0]]
            console.log("visible tweets: ", this.tweetsForTopics)
            console.log("visible tweets: ", this.visibleTweets)
            // const onSelectionMeaasge = selection.length !== 0 ? 'row was selected' : 'row was diselected'
            // alert(onSelectionMeaasge);
          }
        },
        tweets: {},
        tweetsTopics: {},
        tweetsForTopics: {},
        visibleTweets: [],
        isLoading: false,
        error: ''
    }
  },
  methods: {
    async loadTweets(search_query) {
      console.log("Hello from App.vue search_query", search_query)
      this.isLoading = true 
      try {
        console.log("Henlo ")
        this.tweets = await TweetService.getTweets(search_query);
        console.log("this.tweetss ", this.tweets);
        let vv = this.tweets
        this.tweetsTopics = Object.keys(this.tweets).map(function(key) {
          let rObj = []
          // rObj[`${key}`] = vv[`${key}`][0]
          rObj[0] = `${key}`
          rObj[1] = vv[`${key}`][0]
          //stops here
          console.log("rObj; ", rObj)
          return rObj;
        });
        this.tweetsForTopics = Object.keys(this.tweets).map(function(key) {
          let rArr = [`${key}`, vv[`${key}`][1]];
          return rArr;
        });
        console.log("this.tweetsTopics ", this.tweetsTopics)
        console.log("this.tweetsForTopics ", this.tweetsForTopics)
        // delete this.tweets["rt", search_query]
        ;['rt', search_query, search_query.toLowerCase(), '\'', '\' s', '\' m','’ m', '’ s', '’ t', '’ re', '’ ve'].forEach(e => delete this.tweetsTopics[e]);
        search_query.split(" ").forEach(e => delete this.tweetsTopics[e]);
        search_query.toLowerCase().split(" ").forEach(e => delete this.tweetsTopics[e]);
        console.log("Hello from App.vue ", this.tweetsTopics)
        var TObj = this.tweetsTopics
        TObj.splice(0, 0, ['Topics', 'Tweets'])
        TObj = TObj.slice(0,15)
        console.log("Hanlo ", TObj)
        this.chartData = TObj
        this.isLoading = false
        console.log(this.chartData)
      } catch(err) {
        this.error = err.message;
      }
    }
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#loader {
  margin: auto;
  width: 50%;
}

.invisible {
  visibility: hidden
}

</style>