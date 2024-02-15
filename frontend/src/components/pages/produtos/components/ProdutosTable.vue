<script>
  import axios from 'axios';
  import NotificationCard from '../../../general/NotificationCard.vue';

  export default {
    name: 'ProdutosTable',
    components: {
      NotificationCard,
    },
    props: {
      produtos: {
        type: Array,
        default: () => [],
      }
    },
    methods: {
      editProduto(produtoId) {
        this.$router.push(`/produtos/${produtoId}`);
      },
      deleteProduto(produtoId) {
        axios
          .delete(`http://localhost:8000/api/produtos/${produtoId}`)
          .then(() => {
            this.getProdutos();
            this.mostraNotificacao('success', 'Produto removido com sucesso');
            window.location.reload();
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao remover o produto');
          });
      },
      getProdutos(produtos){
        this.produtos = produtos;
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
        <th scope="col">Preço</th>
        <th scope="col">Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="produto in produtos">
        <td>{{produto.nome}}</td>
        <td>R${{produto.preco}}</td>
        <td>
          <button class="btn btn-outline-primary" @click="editProduto(produto.id)">Editar</button>
          <button class="btn btn-outline-danger" @click="deleteProduto(produto.id)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>