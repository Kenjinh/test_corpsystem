<script>
  import axios from 'axios';
  import NotificationCard from '../../general/NotificationCard.vue';
  import ClientesTable from './components/ClientesTable.vue';

  export default {
    name: 'ClientesList',
    data() {
      return {
        clientes: [],
      }
    },
    mounted() {
      this.getClientes();
    },
    components: {
      NotificationCard,
      ClientesTable
    },
    methods: {
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      getClientes() {
        axios
          .get('http://localhost:8000/api/clientes/')
          .then((response) => {
            console.log(response.data);
            this.clientes = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar os clientes');
          });
      },
    },
  };
</script>

<template>
  <div class="container">
    <h1>Clientes</h1>
    <ClientesTable :clientes="clientes" />
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