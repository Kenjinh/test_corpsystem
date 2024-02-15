<script>
  import axios from 'axios';
  import NotificationCard from '../../../general/NotificationCard.vue';

  export default {
    name: 'ClientesTable',
    components: {
      NotificationCard,
    },
    props: {
      clientes: {
        type: Array,
        default: () => [],
      }
    },
    methods: {
      editCliente(clienteId) {
        this.$router.push(`/clientes/${clienteId}`);
      },
      deleteCliente(clienteId) {
        axios
          .delete(`http://localhost:8000/api/clientes/${clienteId}/`)
          .then(() => {
            this.getClientes();
            this.mostraNotificacao('success', 'Cliente removido com sucesso');
            window.location.reload();
          })
          .catch(() => {
            this.mostraNotificacao('error', 'Erro ao remover o cliente');
          });
      },
      getClientes(clientes){
        this.clientes = clientes;
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
        <th scope="col">CPF</th>
        <th scope="col">Telefone</th>
        <th scope="col">Endereço</th>
        <th scope="col">Cidade</th>
        <th scope="col">Estado</th>
        <th scope="col">CEP</th>
        <th scope="col">Data de nascimento</th>
        <th scope="col">Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="cliente in clientes">
        <td>{{cliente.nome}}</td>
        <td>{{cliente.sobrenome}}</td>
        <td>{{cliente.email}}</td>
        <td>{{cliente.cpf}}</td>
        <td>{{cliente.telefone}}</td>
        <td>{{cliente.endereco}}</td>
        <td>{{cliente.cidade}}</td>
        <td>{{cliente.estado}}</td>
        <td>{{cliente.cep}}</td>
        <td>{{cliente.data_nascimento}}</td>
        <td>
          <button class="btn btn-outline-primary" @click="editCliente(cliente.id)">Editar</button>
          <button class="btn btn-outline-danger" @click="deleteCliente(cliente.id)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>