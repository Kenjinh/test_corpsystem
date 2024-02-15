import pytest
from clientes.models import Cliente

@pytest.mark.django_db
def test_client_model_create():
  cliente = Cliente.objects.create(
    nome="Teste", 
    sobrenome="Teste", 
    email="teste@teste", 
    telefone="123456789", 
    cpf="12345678901", 
    data_nascimento="2022-01-01",
    endereco="Rua Teste",
    cidade="Teste",
    estado="SP",
    cep="12345678"
  )
  assert cliente

@pytest.mark.django_db
def test_client_model_str():
  cliente = Cliente.objects.create(
    nome="Teste", 
    sobrenome="Teste", 
    email="teste@teste", 
    telefone="123456789", 
    cpf="12345678901", 
    data_nascimento="2022-01-01",
    endereco="Rua Teste",
    cidade="Teste",
    estado="SP",
    cep="12345678"
  )
  assert str(cliente) == 'Teste Teste'

@pytest.mark.django_db
def test_client_model_update():
  cliente = Cliente.objects.create(
    nome="Teste", 
    sobrenome="Teste", 
    email="teste@teste", 
    telefone="123456789", 
    cpf="12345678901", 
    data_nascimento="2022-01-01",
    endereco="Rua Teste",
    cidade="Teste",
    estado="SP",
    cep="12345678"
  )
  assert cliente
  Cliente.objects.filter(id=cliente.id).update(
    nome="Teste Atualizado"
  )
  clinete_atualizado = Cliente.objects.get(id=cliente.id)
  assert clinete_atualizado.nome == 'Teste Atualizado'

@pytest.mark.django_db
def test_client_model_delete():
  cliente = Cliente.objects.create(
    nome="Teste", 
    sobrenome="Teste", 
    email="teste@teste", 
    telefone="123456789", 
    cpf="12345678901", 
    data_nascimento="2022-01-01",
    endereco="Rua Teste",
    cidade="Teste",
    estado="SP",
    cep="12345678"
  )
  assert cliente
  cliente.delete()
  assert cliente.is_active == False

