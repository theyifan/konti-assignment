<template>
  <div class="country-grid">
    <p class="country">{{ countryName }}</p>
    <b-container class="container-dots flex-row">
      <b-row>
        <span v-for="index in numberOfBrands" :key="index" v-bind:class="{'dot-asian mb-2': asian,  'dot-nonasian mb-2': !asian}"></span>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'CountryGrid',
  props: {
    countryName: String, 
    asian: Boolean, 
    numberOfBrands: Number
  }
}
</script>