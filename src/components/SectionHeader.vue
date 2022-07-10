<template>
  <b-container>
    <b-row>
      <b-col>
        <h2 class="noodle-font pt-5 mb-5 section-title">
          Instand noodle brands are mostly from 
          <span class="highlight">Asia</span>
        </h2>
      </b-col>
    </b-row>
    <b-row class="mb-0">
      <b-col>
        <h4 class="noodle-font mb-2 section-subtitle">
          Distribution of instant noodle brands according to their country of origin
        </h4>
      </b-col>
    </b-row>
    <b-row class="mb-4">
      <b-col>
        <span class="dot-asian mr-2"></span>
        <span class="caption">Asian Country</span>
        <span class="dot-nonasian ml-5 mr-2"></span>
        <span class="caption">Non-Asian Country</span>
      </b-col>
    </b-row>
    <b-row class="mb-4">
      <b-col>
        <p class="caption">
          Each dot represents an instant noodle brand. Click the dot to see the brand.
        </p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: 'SectionHeader',
}
</script>