<template>
  <div id="app">
    <b-container class="inner">
      <SectionHeader />
      <CountryContainer />
      <SectionParagraph />
    </b-container>
  </div>
</template>

<script>
import CountryContainer from './components/CountryContainer.vue'
import SectionHeader from './components/SectionHeader.vue'
import SectionParagraph from './components/SectionParagraph.vue'
import './assets/SectionStyle.css'

export default {
  name: 'App',
  components: {
    CountryContainer, 
    SectionHeader, 
    SectionParagraph
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
  background-color: #FBF4E9;
}

</style>
