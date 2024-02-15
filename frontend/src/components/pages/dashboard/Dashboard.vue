<script>
  import axios from 'axios';
  import VueDatePicker from '@vuepic/vue-datepicker';
  import '@vuepic/vue-datepicker/dist/main.css'
  import NotificationCard from '../../general/NotificationCard.vue';
  import DashTable from './components/DashTable.vue';

  export default {
    name: 'Dashboard',
    components: {
      VueDatePicker,
      NotificationCard,
      DashTable
    },
    data() {
      return {
        selecionarData: null,
        vendedor: null,
        cliente: null,
        vendas: [],
      };
    },
    mounted() {
      this.getVendas();
    },
    methods: {
      async getVendas() {
        const params = {};
        if (this.selecionarData) {
          params.data_inicial = this.formatDate(this.selecionarData[0]);
          params.data_final = this.formatDate(this.selecionarData[1]);
        }
        if (this.vendedor) {
          params.vendedor = this.vendedor;
        }
        await axios
          .get('http://localhost:8000/api/vendas/', { params })
          .then((response) => {
            this.vendas = response.data;
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao carregar as vendas');
          });
      },
      formatDate(date) {
        const year = date.getFullYear();
        let month = date.getMonth() + 1;
        if (month < 10) {
          month = '0' + month;
        }
        let day = date.getDate();
        if (day < 10) {
          day = '0' + day;
        }
        return `${year}-${month}-${day}`;
      },
      mostraNotificacao(type, message) {
        this.$refs.notification.showNotification(type, message);
      },
      addVenda() {
        this.$router.push('/vendas/adicionar');
      }
    },
  };
</script>
<template>
  <div class="container">
    <div class="filters mb-3">
      <VueDatePicker v-model="selecionarData" range :enable-time-picker="false" class="dta-picker"/>
      <div class="input-group">
        <span class="input-group-text" id="inputGroup-sizing-sm">Cliente</span>
        <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" v-model="cliente" placeholder="Cliente" >
      </div>
      <div class="input-group">
        <span class="input-group-text" id="inputGroup-sizing-sm">Vendedor</span>
        <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm"  v-model="vendedor" placeholder="Vendedor" >
      </div>
    </div>
    <button class="adicina-venda btn btn-outline-primary mb-3" @click="addVenda">Adicionar Venda</button>
    <DashTable ref="dashTable" :vendas="vendas" @vendaDeleted="getVendas"/>
    <NotificationCard ref="notification"/>
    <button class="btn btn-outline-primary mb-3" @click="getVendas">Filtrar</button>
    
  </div>
</template>
<style>
.container {
  height: 100vh;
  width: 100%;
}
.filters {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.filters .form-control {
  width: 20%;
}
.dta-picker{
  width: 40%;
}
.container {
  padding: 10vh;
  text-align: center;
}
.adicina-venda {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px;
  border-radius: 5px;
  z-index: 1000;
}
.table {
  border-radius: 20%;
}
</style>