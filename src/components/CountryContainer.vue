<template>
  <b-container>
    <b-row cols="2" cols-md="4" v-for="(_, i) in getNoOfRows" v-bind:key="i">
      <b-col v-for="(country, idx) in getRow(i * 4)" v-bind:key="`country${idx}`" class="mb-3" >
        <CountryGrid 
          v-bind:country-name="country.countryName"
          v-bind:number-of-brands="country.numberOfBrands"
          v-bind:asian="country.asian"
        />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import CountryData from '../helpers/CountryData';
import CountryGrid from './CountryGrid.vue';

export default {
  name: 'CountryContainer',
  components: {
    CountryGrid
  },
  data: function(){
    return {
      countryData: CountryData
    }
  }, 
  computed: {
    getNoOfRows() {
      return Math.ceil(CountryData.length / 4)
    }
  }, 
  methods: {
    getRow(i) {
      return CountryData.slice(i, i+4)
    },
  }
}
</script>

<style scoped>
</style>