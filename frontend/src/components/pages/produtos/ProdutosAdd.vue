<script>
  import axios from 'axios';
  import NotificationCard from '../../general/NotificationCard.vue';

  export default {
    name: 'ProdutosAdd',
    data() {
      return {
        produto: {
          'nome': null,
          'preco': null,
        },
      }
    },
    components: {
      NotificationCard,
    },
    methods: {
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      adicionaProduto() {
        axios
          .post('http://localhost:8000/api/produtos/', this.produto)
          .then(() => {
            this.mostraNotificacao('success', 'Produto adicionado com sucesso');
            window.location.reload();
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao adicionar o produto');
          });
      },
  },
}
</script>
<template>
  <div class="container">
    <h1>Adicionar Produto</h1>
    <form class="mb-3">
      <div class="mb-3">
        <label for="nome" class="from-label">Nome</label>
        <input type="text" class="form-control" id="nome" v-model="produto.nome" placeholder="Nome">
      </div>
      <div class="mb-3">
        <label for="sobrenome" class="from-label">Preço</label>
        <input type="text" class="form-control" id="sobrenome" v-model="produto.preco" placeholder="Preço">
      </div>
    </form>
    <div class="form-footer">
      <button class="btn btn-primary" @click="adicionaProduto">Adicionar Produto</button>
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