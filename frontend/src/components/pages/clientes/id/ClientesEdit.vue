<script>
  import axios from 'axios';
  import NotificationCard from '../../../general/NotificationCard.vue';

  export default {
    name: 'ClienteEdit',
    data() {
      return {
        clienteId: this.$route.params.id,
        cliente: {
          'nome': null,
          'sobrenome': null,
          'email': null,
          'cpf': null,
          'telefone': null,
          'endereco': null,
          'cidade': null,
          'estado': null,
          'cep': null,
          'data_nascimento': null,
        },
      }
    },
    mounted() {
      this.getCliente();
    },
    components: {
      NotificationCard,
    },
    methods: {
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      async getCliente() {
        await axios
          .get(`http://localhost:8000/api/clientes/${this.clienteId}/`)
          .then((response) => {
            this.cliente = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar o cliente');
          });
      },
      editarCliente() {
        axios
          .put(`http://localhost:8000/api/clientes/${this.clienteId}/`, this.cliente)
          .then(() => {
            this.mostraNotificacao('success', 'Cliente adicionado com sucesso');
            this.$router.push('/clientes');
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao adicionar o cliente');
          });
      },
  },
}
</script>
<template>
  <div class="container">
    <h1>Editar Cliente</h1>
    <form class="mb-3">
      <div class="mb-3">
        <label for="nome" class="from-label">Nome</label>
        <input type="text" class="form-control" id="nome" v-model="cliente.nome" placeholder="Nome">
      </div>
      <div class="mb-3">
        <label for="sobrenome" class="from-label">Sobrenome</label>
        <input type="text" class="form-control" id="sobrenome" v-model="cliente.sobrenome" placeholder="Sobrenome">
      </div>
      <div class="mb-3">
        <label for="email" class="from-label">Email</label>
        <input type="text" class="form-control" id="email" v-model="cliente.email" placeholder="Email">
      </div>
      <div class="mb-3">
        <label for="cpf" class="from-label">CPF</label>
        <input type="text" min="11" max="11" class="form-control" id="cpf" v-model="cliente.cpf" placeholder="CPF">
      </div>
      <div class="mb-3">
        <label for="telefone" class="from-label">Telefone</label>
        <input type="text" class="form-control" id="telefone" v-model="cliente.telefone" placeholder="Telefone">
      </div>
      <div class="mb-3">
        <label for="data_nascimento" class="from-label">Data de Nascimento</label>
        <input type="date" class="form-control" id="data_nascimento" v-model="cliente.data_nascimento">
      </div>
      <div class="mb-3">
        <label for="endereco" class="from-label">Endereço</label>
        <input type="text" class="form-control" id="endereco" v-model="cliente.endereco" placeholder="Endereço">
      </div>
      <div class="mb-3">
        <label for="cidade" class="from-label">Cidade</label>
        <input type="text" class="form-control" id="cidade" v-model="cliente.cidade" placeholder="Cidade">
      </div>
      <div class="mb-3">
        <label for="estado" class="from-label">Estado</label>
        <input type="text" class="form-control" id="estado" v-model="cliente.estado" placeholder="Estado">
      </div>
      <div class="mb-3">
        <label for="cep" class="from-label">CEP</label>
        <input type="text" class="form-control" id="cep" v-model="cliente.cep" placeholder="CEP">
      </div>
    </form>
    <div class="form-footer">
      <button class="btn btn-primary" @click="editarCliente">Editar</button>
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