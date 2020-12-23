<template>
  <div @click.self="$emit('close')" class="modal-overlay">
    <div class="modal-container">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
}
</script>

<style>
.modal-overlay {
  background-color: #0000004a;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  z-index: 999999999999;
  position: fixed;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-line-pack: baseline;
  align-content: baseline;
}

.modal-container {
  background-color: #fff;
  border-radius: 1rem;
  width: 286px;
  height: auto;
  box-shadow: #0000004a 0px 3px 8px 0px;
  padding: 1em;
}
</style>
