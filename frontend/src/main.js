import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('./components/pages/dashboard/Dashboard.vue')
  },
  {
    path: '/vendas/adicionar',
    name: 'Adicionar Venda',
    component: () => import('./components/pages/vendas/VendasAdd.vue')
  },
  {
    path: '/vendas/:id',
    name: 'Editar Venda',
    component: () => import('./components/pages/vendas/id/VendasEdit.vue')
  },
  {
    path: '/clientes',
    name: 'Listar Clientes',
    component: () => import('./components/pages/clientes/ClientesList.vue')
  },
  {
    path: '/clientes/:id',
    name: 'Editar Cliente',
    component: () => import('./components/pages/clientes/id/ClientesEdit.vue')
  },
  {
    path: '/clientes/adicionar',
    name: 'Adicionar Cliente',
    component: () => import('./components/pages/clientes/ClientesAdd.vue')
  },
  {
    path: '/vendedores',
    name: 'Listar Vendedores',
    component: () => import('./components/pages/vendedores/VendedoresList.vue')
  },
  {
    path: '/vendedores/:id',
    name: 'Editar Vendedor',
    component: () => import('./components/pages/vendedores/id/VendedoresEdit.vue')
  },
  {
    path: '/vendedores/adicionar',
    name: 'Adicionar Vendedor',
    component: () => import('./components/pages/vendedores/VendedoresAdd.vue')
  },
  {
    path: '/produtos',
    name: 'Listar Produtos',
    component: () => import('./components/pages/produtos/ProdutosList.vue')
  },
  {
    path: '/produtos/:id',
    name: 'Editar Produto',
    component: () => import('./components/pages/produtos/id/ProdutosEdit.vue')
  },
  {
    path: '/produtos/adicionar',
    name: 'Adicionar Produto',
    component: () => import('./components/pages/produtos/ProdutosAdd.vue')
  },
  {
    path: '/relatorio',
    name: 'Relatorio',
    component: () => import('./components/pages/relatorio/Relatorio.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
});

createApp(App).use(router).mount('#app')
