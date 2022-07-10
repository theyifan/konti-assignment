<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <CountryContainer/>
  </div>
</template>

<script>
import CountryContainer from './components/CountryContainer.vue'

export default {
  name: 'App',
  components: {
    CountryContainer
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Poppins');

#app {
  font-family: Poppins, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
