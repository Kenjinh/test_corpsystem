<script>
  import axios from 'axios';
  import NotificationCard from '../../general/NotificationCard.vue';

  export default {
    name: 'VendasEdit',
    data() {
      return {
        vendaId: this.$route.params.id,
        venda:{
          "venda": {
            "cliente": null,
            "vendedor": null,
            "data": null,
            "pagamento": null,
            "total": null
          },
          "produtos": []
        },
        vendedores: [],
        clientes: [],
        produtos: [],
        novoProduto: {
          'produto': null,
          'quantidade': null,
        },
      };
    },
    components: {
      NotificationCard,
    },
    mounted() {
      this.getVendedors();
      this.getCliente();
      this.getProdutos();
    },
    methods: {
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      async getVendedors() {
        await axios
          .get('http://localhost:8000/api/vendedores/')
          .then((response) => {
            this.vendedores = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar os vendedores');
          });
      },
      async getCliente() {
        await axios
          .get('http://localhost:8000/api/clientes/')
          .then((response) => {
            this.clientes = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar os clientes');
          });
      },
      async getProdutos() {
        await axios
          .get('http://localhost:8000/api/produtos/')
          .then((response) => {
            this.produtos = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar os produtos');
          });
      },
      removerProduto(indice) {
        for (let i = 0; i < this.produtos.length; i++) {
          if (this.produtos[i].id === this.venda.produtos[indice].produto) {
            this.venda.venda.total -= this.produtos[i].preco * this.venda.produtos[indice].quantidade;
          }
        }
        console.log(this.venda.venda.total)
        this.venda.produtos.splice(indice, 1);
      },
      adicionarProduto() {
        const novoItem = {
          'produto': this.novoProduto.produto,
          'quantidade': this.novoProduto.quantidade,
        }
        for (let i = 0; i < this.produtos.length; i++) {
          if (this.produtos[i].id === this.novoProduto.produto) {
            this.venda.venda.total += this.produtos[i].preco * this.novoProduto.quantidade;
          }
        }
        this.venda.produtos.push(novoItem);
        this.novoProduto.produto = null;
        this.novoProduto.quantidade = null;
      },
      adicionaVenda() {
        axios.post('http://localhost:8000/api/vendas/', this.venda)
          .then(() => {
            this.mostraNotificacao('success', 'Venda adicionada com sucesso');
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao adicionar a venda');
          });
        this.$router.push('/vendas/adicionar');
      },
  },
}
</script>
<template>
  <div class="container">
    <h1>Adicionar Venda</h1>
    <form class="mb-3">
      <div class="mb-3">
        <label for="cliente" class="from-label">Cliente</label>
        <select class="form-select" v-model="venda.venda.cliente">
          <option v-for="cliente in clientes" :key="cliente.id" :value="cliente.id">{{ cliente.nome }} {{ cliente.sobrenome }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="cliente" class="from-label">Vendedor</label>
        <select class="form-select" v-model="venda.venda.vendedor">
          <option v-for="vendedor in vendedores" :key="vendedor.id" :value="vendedor.id">{{ vendedor.nome }} {{ vendedor.sobrenome }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="cliente" class="from-label">Total</label>
        <input type="text" readonly v-model="venda.venda.total" class="form-control">
      </div>
      <div class="mb-3">
        <label for="cliente" class="from-label">Forma de Pagamento</label>
        <select class="form-select" v-model="venda.venda.pagamento">
          <option value="dinheiro">Dinheiro</option>
          <option value="cartao">Cartão</option>
          <option value="cheque">Cheque</option>
          <option value="boleto">Boleto</option>
          <option value="pix">Pix</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="cliente" class="from-label">Status</label>
        <select class="form-select" v-model="venda.venda.status">
          <option value="pago">Pago</option>
          <option value="pendente">Pendente</option>
          <option value="cancelado">Cancelado</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="cliente" class="from-label">Data</label>
        <input type="date" v-model="venda.venda.data" class="form-control">
      </div>
      <div class="mb-3">
        <label for="cliente" class="from-label">Produtos</label>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Produto</th>
              <th scope="col">Quantidade</th>
              <th scope="col">Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="produto in venda.produtos">
              <th>
                <select class="form-select" v-model="produto.produto">
                  <option v-for="prod in produtos" :key="prod.id" :value="prod.id">{{ prod.nome }} - R${{ prod.preco }}</option>
                </select>
              </th>
              <td>
                <input type="number" min="1" step="1" placeholder="Quantidade" v-model="produto.quantidade" class="form-control">
              </td>
              <td>
                <button class="btn btn-danger" @click="removerProduto(venda.produtos.indexOf(produto))">Remover</button>
              </td>
            </tr>
            <tr>
              <td>
                <select class="form-select" v-model="novoProduto.produto">
                  <option v-for="prod in produtos" :key="prod.id" :value="prod.id">{{ prod.nome }} - R${{ prod.preco }}</option>
                </select>
              </td>
              <td>
                <input type="number" min="1" step="1" placeholder="Quantidade" v-model="novoProduto.quantidade" class="form-control">
              </td>
              <td colspan="3">
                <button class="btn btn-primary" @click.prevent="adicionarProduto">Adicionar</button>
              </td>
            </tr>
          </tbody>
        </table>

      </div>
    </form>
    <div class="form-footer">
      <button class="btn btn-primary" @click="adicionaVenda">Adicionar Venda</button>
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