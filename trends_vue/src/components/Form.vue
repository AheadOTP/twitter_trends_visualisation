<template>
  <div>	
      <div><div class="error_message">{{this.error_message}}</div></div>
      <input id="query" v-model="search_query" placeholder="edit me">
      <p>Message is: {{ this.search_query }}</p>
      <button v-on:click="onClickSearch()">Search</button>
  </div>
</template>

<script>
export default {
  name: 'Form',
  data: function () {
    return {
      search_query: "",
      error_message: ""
    }
  },
  methods: {
    onClickSearch () {
      if (this.search_query == "") {
        this.error_message = "Query can't be empty!"
      } else {
        this.error_message = ""
        console.log("Hello from Form.vue ", this.search_query)
        this.$emit('parentSearch', this.search_query)
      }
    }
  },
  props: ['loadTweets']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.error_message {
  color:white;
  background-color: red;
  display: inline-block;
}
</style>
