<script>
  import axios from 'axios';
  import NotificationCard from '../../general/NotificationCard.vue';
  import ProdutosTable from './components/ProdutosTable.vue';

  export default {
    name: 'ProdutosList',
    data() {
      return {
        produtos: [],
      }
    },
    mounted() {
      this.getProdutos();
    },
    components: {
      NotificationCard,
      ProdutosTable
    },
    methods: {
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      getProdutos() {
        axios
          .get('http://localhost:8000/api/produtos/')
          .then((response) => {
            this.produtos = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar os produtos');
          });
      },
    },
  };
</script>

<template>
  <div class="container">
    <h1>Produtos</h1>
    <ProdutosTable :produtos="produtos" />
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