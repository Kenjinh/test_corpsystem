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
    title: 'Dashboard',
    component: () => import('./components/pages/dashboard/Dashboard.vue'),
    meta: {
      title: 'Vendas - Dashboard',
      requiredAuth: true,
    }
  },
  {
    path: '/vendas/adicionar',
    name: 'Adicionar Venda',
    component: () => import('./components/pages/vendas/VendasAdd.vue'),
    meta: {
      title: 'Vendas - Adicionar Venda',
      requiredAuth: true,
    }
  },
  {
    path: '/vendas/:id',
    name: 'Editar Venda',
    component: () => import('./components/pages/vendas/id/VendasEdit.vue'),
    meta: {
      title: 'Vendas - Editar Venda',
      requiredAuth: true,
    }
  },
  {
    path: '/clientes',
    name: 'Listar Clientes',
    component: () => import('./components/pages/clientes/ClientesList.vue'),
    meta: {
      title: 'Vendas - Listar Clientes',
      requiredAuth: true,
    }
  },
  {
    path: '/clientes/:id',
    name: 'Editar Cliente',
    component: () => import('./components/pages/clientes/id/ClientesEdit.vue'),
    meta: {
      title: 'Vendas - Editar Cliente',
      requiredAuth: true,
    }
  },
  {
    path: '/clientes/adicionar',
    name: 'Adicionar Cliente',
    component: () => import('./components/pages/clientes/ClientesAdd.vue'),
    meta: {
      title: 'Vendas - Adicionar Cliente',
      requiredAuth: true,
    }
  },
  {
    path: '/vendedores',
    name: 'Listar Vendedores',
    component: () => import('./components/pages/vendedores/VendedoresList.vue'),
    meta: {
      title: 'Vendas - Listar Vendedores',
      requiredAuth: true,
    }
  },
  {
    path: '/vendedores/:id',
    name: 'Editar Vendedor',
    component: () => import('./components/pages/vendedores/id/VendedoresEdit.vue'),
    meta: {
      title: 'Vendas - Editar Vendedor',
      requiredAuth: true,
    }
  },
  {
    path: '/vendedores/adicionar',
    name: 'Adicionar Vendedor',
    component: () => import('./components/pages/vendedores/VendedoresAdd.vue'),
    meta: {
      title: 'Vendas - Adicionar Vendedor',
      requiredAuth: true,
    }
  },
  {
    path: '/produtos',
    name: 'Listar Produtos',
    component: () => import('./components/pages/produtos/ProdutosList.vue'),
    meta: {
      title: 'Vendas - Listar Produtos',
      requiredAuth: true,
    }
  },
  {
    path: '/produtos/:id',
    name: 'Editar Produto',
    component: () => import('./components/pages/produtos/id/ProdutosEdit.vue'),
    meta: {
      title: 'Vendas - Editar Produto',
      requiredAuth: true,
    }
  },
  {
    path: '/produtos/adicionar',
    name: 'Adicionar Produto',
    component: () => import('./components/pages/produtos/ProdutosAdd.vue'),
    meta: {
      title: 'Vendas - Adicionar Produto',
      requiredAuth: true,
    }
  },
  {
    path: '/relatorio',
    name: 'Relatorio',
    component: () => import('./components/pages/relatorio/Relatorio.vue'),
    meta: {
      title: 'Vendas - Relatorio',
      requiredAuth: true,
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('./components/pages/auth/LoginPage.vue'),
    meta: {
      title: 'Vendas - Login',
    }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Vendas'
  if (to.meta.requiredAuth) {
    const token_store = localStorage.getItem('token')
    if (!token_store) {
      next({ name: 'Login' })
    } 
    else {
      const token = JSON.parse(token_store)
      const now = new Date()
      if (token.expiry < now.getTime()) {
        localStorage.removeItem('token')
        next({ name: 'Login' })
      }
      next()
    }
  }
  next()
})

createApp(App).use(router).mount('#app')
