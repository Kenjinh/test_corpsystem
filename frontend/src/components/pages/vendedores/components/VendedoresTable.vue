<script>
  import axios from 'axios';
  import NotificationCard from '../../../general/NotificationCard.vue';

  export default {
    name: 'vendedoresTable',
    components: {
      NotificationCard,
    },
    props: {
      vendedores: {
        type: Array,
        default: () => [],
      }
    },
    methods: {
      editVendedor(vendedorId) {
        this.$router.push(`/vendedores/${vendedorId}`);
      },
      deleteVendedor(vendedorId) {
        axios
          .delete(`http://localhost:8000/api/vendedores/${vendedorId}`)
          .then(() => {
            this.getVendedores();
            this.mostraNotificacao('success', 'Cliente removido com sucesso');
            window.location.reload();
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao remover o cliente');
          });
      },
      getVendedores(vendedores){
        this.vendedores = vendedores;
      },
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      }
    }
  };
</script>
<template>
  <table class="table">
    <thead>
      <tr>
        <th scope="col">Nome</th>
        <th scope="col">Sobrenome</th>
        <th scope="col">Email</th>
        <th scope="col">Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="vendedor in vendedores">
        <td>{{vendedor.nome}}</td>
        <td>{{vendedor.sobrenome}}</td>
        <td>{{vendedor.email}}</td>
        <td>
          <button class="btn btn-outline-primary" @click="editVendedor(vendedor.id)">Editar</button>
          <button class="btn btn-outline-danger" @click="deleteVendedor(vendedor.id)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>