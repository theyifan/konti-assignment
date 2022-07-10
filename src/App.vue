<template>
  <div id="app">
    <SectionHeader />
    <CountryContainer />
  </div>
</template>

<script>
import CountryContainer from './components/CountryContainer.vue'
import SectionHeader from './components/SectionHeader.vue'
import './assets/SectionStyle.css'

export default {
  name: 'App',
  components: {
    CountryContainer, 
    SectionHeader
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
  color: rgba(0, 0, 0, 0.7);
  margin-top: 60px;
}

</style>
