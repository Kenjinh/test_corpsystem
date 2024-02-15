<script setup>
  import { RouterView } from 'vue-router';
  import Header from './components/general/Header.vue';
</script>

<template>
  <div id="app">
    <Header/>
    <RouterView/>
  </div>
</template>

<style scoped>
</style>
