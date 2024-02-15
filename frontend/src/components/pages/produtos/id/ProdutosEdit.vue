<script>
  import axios from 'axios';
  import NotificationCard from '../../../general/NotificationCard.vue';

  export default {
    name: 'ProdutosEdit',
    data() {
      return {
        produtoId: this.$route.params.id,
        produto: {
          'nome': null,
          'preco': null,
        },
      }
    },
    mounted() {
      this.getProduto();
    },
    components: {
      NotificationCard,
    },
    methods: {
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      async getProduto() {
        await axios
          .get(`http://localhost:8000/api/produtos/${this.produtoId}`)
          .then((response) => {
            this.produto = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar o produto');
          });
      },
      editarProduto() {
        axios
          .put(`http://localhost:8000/api/produtos/${this.produtoId}`, this.produto)
          .then(() => {
            this.mostraNotificacao('success', 'Produto adicionado com sucesso');
            window.location.reload();
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao adicionar o vendedor');
          });
      },
  },
}
</script>
<template>
  <div class="container">
    <h1>Editar Produto</h1>
    <form class="mb-3">
      <div class="mb-3">
        <label for="nome" class="from-label">Nome</label>
        <input type="text" class="form-control" id="nome" v-model="produto.nome" placeholder="Nome">
      </div>
      <div class="mb-3">
        <label for="preco" class="from-label">Preço</label>
        <input type="text" class="form-control" id="preco" v-model="produto.preco" placeholder="Preço">
      </div>
    </form>
    <div class="form-footer">
      <button class="btn btn-primary" @click="editarProduto">Editar</button>
    </div>
    <NotificationCard ref="notification" />
  </div>
</template>
<style>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 50%;
  min-height: 100vh;
  height: auto;
  margin: 0 auto;
  padding: 10px;
}
.container h1 {
  text-align: center;
  margin: 20px;
}
.form-footer {
  display: flex;
  justify-content: center;
}
</style>