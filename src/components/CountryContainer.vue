<template>
  <b-container class="mb-4">
    <b-row cols="2" cols-md="4" v-for="(_, i) in noOfRows" v-bind:key="i">
      <b-col v-for="(country, idx) in getRow(i * 4)" v-bind:key="`country${idx}`" class="mb-3" >
        <CountryGrid 
          v-bind:country-name="country.countryName"
          v-bind:number-of-brands="country.numberOfBrands"
          v-bind:asian="country.asian"
          v-bind:brands="country.brands"
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
    noOfRows() {
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