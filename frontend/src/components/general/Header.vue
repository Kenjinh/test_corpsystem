<script >
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/">Dashboard</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Clientes
            </a>
            <ul class="dropdown-menu">
              <li class="dropdown-item"><a class="dropdown-link" href="/clientes">Listar Clientes</a></li>
              <li class="dropdown-item"><a class="dropdown-link" href="/clientes/adicionar">Adicionar Cliente</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Vendedores
            </a>
            <ul class="dropdown-menu">
              <li class="dropdown-item"><a class="dropdown-link" href="/vendedores">Listar Vendedores</a></li>
              <li class="dropdown-item"><a class="dropdown-link" href="/vendedores/adicionar">Adicionar Vendedor</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Produtos
            </a>
            <ul class="dropdown-menu">
              <li class="dropdown-item"><a class="dropdown-link" href="/produtos">Listar Produtos</a></li>
              <li class="dropdown-item"><a class="dropdown-link" href="/produtos/adicionar">Adicionar Produto</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/relatorio">Relatório</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style>
</style>
