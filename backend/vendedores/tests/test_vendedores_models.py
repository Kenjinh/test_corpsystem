import pytest
from vendedores.models import Vendedores

@pytest.mark.django_db
def test_vendedor_model_create():
  vendedor = Vendedores.objects.create(
    nome="Teste", 
    sobrenome="Teste", 
    email="teste@teste",
  )
  assert vendedor

@pytest.mark.django_db
def test_vendedor_model_str():
  vendedor = Vendedores.objects.create(
    nome="Teste", 
    sobrenome="Teste", 
    email="teste@teste",
  )
  assert str(vendedor) == 'Teste Teste'

@pytest.mark.django_db
def test_vendedores_model_update():
  vendedor = Vendedores.objects.create(
    nome="Teste", 
    sobrenome="Teste", 
    email="teste@teste",
  )
  assert vendedor
  Vendedores.objects.filter(id=vendedor.id).update(
    nome="Teste Atualizado"
  )
  vendedor_atualizado = Vendedores.objects.get(id=vendedor.id)
  assert vendedor_atualizado.nome == 'Teste Atualizado'

@pytest.mark.django_db
def test_vendedores_model_delete():
  vendedor = Vendedores.objects.create(
    nome="Teste", 
    sobrenome="Teste", 
    email="teste@teste",
  )
  assert vendedor
  vendedor.delete()
  assert vendedor.is_active == False
  