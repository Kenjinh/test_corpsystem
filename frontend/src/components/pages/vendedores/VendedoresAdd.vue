<script>
  import axios from 'axios';
  import NotificationCard from '../../general/NotificationCard.vue';

  export default {
    name: 'VendedoresAdd',
    data() {
      return {
        vendedor: {
          'nome': null,
          'sobrenome': null,
          'email': null,
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
      adicionaVendedor() {
        axios
          .post('http://localhost:8000/api/vendedores/', this.vendedor)
          .then(() => {
            this.mostraNotificacao('success', 'Vendedor adicionado com sucesso');
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao adicionar o vendedor');
          });
        this.$router.push('/vendedores/adicionar');
      },
  },
}
</script>
<template>
  <div class="container">
    <h1>Adicionar Vendedor</h1>
    <form class="mb-3">
      <div class="mb-3">
        <label for="nome" class="from-label">Nome</label>
        <input type="text" class="form-control" id="nome" v-model="vendedor.nome" placeholder="Nome">
      </div>
      <div class="mb-3">
        <label for="sobrenome" class="from-label">Sobrenome</label>
        <input type="text" class="form-control" id="sobrenome" v-model="vendedor.sobrenome" placeholder="Sobrenome">
      </div>
      <div class="mb-3">
        <label for="email" class="from-label">Email</label>
        <input type="text" class="form-control" id="email" v-model="vendedor.email" placeholder="Email">
      </div>
    </form>
    <div class="form-footer">
      <button class="btn btn-primary" @click="adicionaVendedor">Adicionar Vendedor</button>
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