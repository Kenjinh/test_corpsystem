<script setup>
  import { RouterView } from 'vue-router';
  import Header from './components/general/Header.vue';
  import { onBeforeMount } from 'vue';
  onBeforeMount(() => {
    const favicon = document.querySelector('link[rel="icon"]');
    favicon.href = '/favicon.ico';
  });
</script>

<template>
  <div id="app">
    <Header/>
    <RouterView/>
  </div>
</template>

<style scoped>
</style>
