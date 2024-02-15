<script>
  import axios from 'axios';
  import NotificationCard from '../../../general/NotificationCard.vue';

  export default {
    name: 'ClienteEdit',
    data() {
      return {
        vendedorId: this.$route.params.id,
        vendedor: {
          'nome': null,
          'sobrenome': null,
          'email': null,
        },
      }
    },
    mounted() {
      this.getVendedor();
    },
    components: {
      NotificationCard,
    },
    methods: {
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      async getVendedor() {
        await axios
          .get(`http://localhost:8000/api/vendedores/${this.vendedorId}`)
          .then((response) => {
            this.vendedor = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar o vendedor');
          });
      },
      editarVendedor() {
        axios
          .put(`http://localhost:8000/api/vendedores/${this.vendedorId}`, this.vendedor)
          .then(() => {
            this.mostraNotificacao('success', 'Vendedor adicionado com sucesso');
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
    <h1>Editar vendedor</h1>
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
      <button class="btn btn-primary" @click="editarVendedor">Editar</button>
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