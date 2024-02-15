<script>
  import axios from 'axios';
  import NotificationCard from '../../general/NotificationCard.vue';
  import VendedoresTable from './components/VendedoresTable.vue';

  export default {
    name: 'VendedoresList',
    data() {
      return {
        vendedores: [],
      }
    },
    mounted() {
      this.getVendedores();
    },
    components: {
      NotificationCard,
      VendedoresTable
    },
    methods: {
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      getVendedores() {
        axios
          .get('http://localhost:8000/api/vendedores/')
          .then((response) => {
            this.vendedores = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar os vendedores');
          });
      },
    },
  };
</script>

<template>
  <div class="container">
    <h1>Vendedores</h1>
    <VendedoresTable :vendedores="vendedores" />
    <NotificationCard ref="notification" />
  </div>
</template>

<style>
.container {
  width: 100%;
  min-height: 100vh;
  height: auto;
  padding: 10px;
}
.container h1 {
  text-align: center;
  margin: 20px;
}
</style>