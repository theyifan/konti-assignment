<template>
  <div class="country-grid">
    <p class="country">{{ countryName }}</p>
    <b-container class="container-dots flex-row">
      <b-row>
        <BrandDot
          v-for="(_, index) in numberOfBrands" :key="`tooltip-${countryName}-${index}`"
          :asian="asian"
          :brand="brands[index]"
        >
        </BrandDot>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import BrandDot from './BrandDot.vue';

export default {
  name: 'CountryGrid',
  components: {
    BrandDot,
  },
  props: {
    countryName: String, 
    asian: Boolean, 
    numberOfBrands: Number, 
    brands: Array,
  }
}
</script>