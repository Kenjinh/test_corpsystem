<script>
  import axios from 'axios';
  import NotificationCard from '../../general/NotificationCard.vue';
  export default {
    name: 'Relatorio',
    components: {
      NotificationCard
    },
    data() {
      return {
        data_inicial: null,
        data_final: null,
        vendedor: null,
        cliente: null,
        data: null,
        method: 'pdf',
        relatorio: [],
        vendedores: [],
        clientes: [],
      }
    },
    mounted() {
      this.getVendedores();
      this.getClientes();
    },
    methods: {
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      getRelatorio() {
        axios
          .get(`http://localhost:8000/api/relatorios/relatorio_vendas`, 
          {
            params: 
            {
              data_inicial: this.data_inicial, 
              data_final: this.data_final, 
              vendedor: this.vendedor,
              cliente: this.cliente,
              data: this.data,
              method: this.method
            },
            responseType: 'blob'
          })
          .then((response) => {
            const blob = new Blob([response.data], { type: `application/${response.headers['content-type']}` }); // Supondo que seja um PDF, ajuste conforme o tipo de arquivo
            const href = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = href;
            if (response.headers['content-type'] === 'application/pdf') {
              link.download = 'relatorio.pdf';
            }
            else if (response.headers['content-type'] === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') {
              link.download = 'relatorio.xlsx';
            }
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar o relatório');
          });
      },
      getVendedores() {
        axios
          .get(`http://localhost:8000/api/vendedores/`)
          .then((response) => {
            this.vendedores = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar os vendedores');
          });
      },
      getClientes() {
        axios
          .get(`http://localhost:8000/api/clientes/`)
          .then((response) => {
            this.clientes = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar os clientes');
          });
      }
    }
  }

</script>

<template>
  <div class="container">
    <h1>Relatório</h1>
    <NotificationCard ref="notification" />
    <div class="mb-3">
      <label for="format" class="from-label">Format</label>
      <select class="form-select" v-model="method">
        <option value="pdf">PDF</option>
        <option value="excel">Excel</option>
      </select>
    </div>
    <div class="mb-3">
      <label for="data_inicial" class="from-label">Data inicial</label>
      <input type="date" class="form-control" id="data_inicial" v-model="data_inicial">
    </div>
    <div class="mb-3">
      <label for="data_final" class="from-label">Data final</label>
      <input type="date" class="form-control" id="data_final" v-model="data_final">
    </div>
    <div class="mb-3">
      <label for="vendedor" class="from-label">Vendedor</label>
      <select class="form-select" v-model="vendedor">
        <option v-for="vendedor in vendedores" :key="vendedor.id" :value="vendedor.id">{{ vendedor.nome }}</option>
      </select>
    </div>
    <div class="mb-3">
      <label for="cliente" class="from-label">Cliente</label>
      <input type="text" class="form-control" id="cliente" v-model="cliente">
    </div>
    <div class="mb-3">
      <label for="data" class="from-label">Data</label>
      <input type="date" class="form-control" id="data" v-model="data">
    </div>
    <div class="form-footer">
      <button class="btn btn-primary" @click="getRelatorio">Gerar</button>
    </div>
  </div>
</template>

<style>
.container {
  width: 100%;
  min-height: 100vh;
  height: auto;
  padding: 10px;
}
</style>