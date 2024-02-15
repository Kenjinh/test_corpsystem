<script>
  import axios from 'axios';
  import NotificationCard from '../../../general/NotificationCard.vue';

  export default {
    name: 'DashTable',
    components: {
      NotificationCard,
    },
    props: {
      vendas: {
        type: Array,
        default: () => [],
      }
    },
    methods: {
      editVenda(vendId) {
        this.$router.push(`/vendas/${vendId}`);
      },
      deleteVenda(vendId) {
        axios
          .delete(`http://localhost:8000/api/vendas/${vendId}/`)
          .then(() => {
            this.getVendas();
            this.mostraNotificacao('success', 'Venda removida com sucesso');
            window.location.reload()
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao remover a venda');
          });
      },
      getVendas(vendas){
        this.vendas = vendas;
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
        <th scope="col">ID</th>
        <th scope="col">Cliente</th>
        <th scope="col">Vendedor</th>
        <th scope="col">Total</th>
        <th scope="col">Pagamento</th>
        <th scope="col">Status</th>
        <th scope="col">Data</th>
        <th scope="col">Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="venda in vendas">
        <th scope="row">{{venda.id}}</th>
        <td>{{venda.cliente_name}}</td>
        <td>{{venda.vendedor_name}}</td>
        <td>R${{venda.total}}</td>
        <td>{{venda.pagamento}}</td>
        <td>{{venda.status}}</td>
        <td>{{venda.data}}</td>
        <td>
          <button class="btn btn-outline-primary" @click="editVenda(venda.id)">Editar</button>
          <button class="btn btn-outline-danger" @click="deleteVenda(venda.id)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>