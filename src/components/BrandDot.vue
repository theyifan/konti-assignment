<template>
  <div class="brand-dot">
    <span 
      :class="{'dot-asian': asian, 'dot-nonasian': !asian}"
    >
    </span>
    <span class="brand-tooltip">
      {{ brand }} 
    </span>
  </div>
</template>

<script>
export default {
  name: 'BrandDot',
  props: {
    asian: Boolean, 
    brand: String
  }
}
</script>

<style scoped>
.brand-dot {
  position: relative; 
  margin-bottom: -1px;
}

.brand-dot .brand-tooltip {
  visibility: hidden;
  width: relative;
  box-shadow: 0 0 8px rgba(0,0,0,.07),0 8px 8px rgba(0,0,0,.07);
  background: white;
  text-align: center;
  padding: 5px 10px;
  border-radius: 6px;
  white-space: nowrap;

  position: absolute;
  z-index: 1;
  bottom: 100%;
  left: 25%;

  opacity: 0;
  transition: opacity 0.2s;
}

.brand-dot:hover .brand-tooltip {
  visibility: visible;
  opacity: 1;
}

.brand-dot .dot-asian:hover {
  border: 1.5px solid #db900d; 
}

.brand-dot .dot-nonasian:hover {
  border: 1.5px solid #b0b0b0; 
}
</style>