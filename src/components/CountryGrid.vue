<template>
  <div class="country-grid">
    <p class="country">{{ countryName }}</p>
    <b-container class="container-dots flex-row">
      <b-row>
        <span v-for="index in numberOfBrands" :key="index" v-bind:class="{'dot-asian': asian,  'dot-nonasian': !asian}"></span>
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

<style scoped>
.country {
  margin-bottom: 10px;
  font-weight: 700;
  font-size: 15px;
}

.container-dots {
  padding-top: 5px;
  margin-right: 15px;
}

.dot-asian {
  height: 10px;
  width: 10px;
  margin-right: 7px;
  margin-bottom: 7px;
  background-color: #f5b817;
  border-radius: 50%;
  display: inline-block;
  position: relative;
}

.dot-nonasian {
  height: 10px;
  width: 10px;
  margin-right: 7px;
  margin-bottom: 7px;
  background-color: #dedede;
  border-radius: 50%;
  display: inline-block;
  position: relative;
}
</style>