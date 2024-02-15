import pytest

@pytest.mark.django_db
def test_listar_vendedores(client):
  response = client.get('/api/vendedores/')
  assert response.status_code == 200

@pytest.mark.django_db
def test_criar_vendedor(client):
  response = client.post('/api/vendedores/', {'nome': 'Teste', 'sobrenome': 'Teste', 'email': 'teste@teste.com'})
  assert response.status_code == 201

@pytest.mark.django_db
def test_detalhar_vendedor(client):
  client.post('/api/vendedores/', {'nome': 'Teste', 'sobrenome': 'Teste', 'email': 'teste@teste.com'})
  response = client.get('/api/vendedores/1/')
  assert response.status_code == 200

@pytest.mark.django_db
def test_editar_vendedor(client):
  client.post('/api/vendedores/', {'nome': 'Teste', 'sobrenome': 'Teste', 'email': 'teste@teste.com'})
  response = client.get('/api/vendedores/1/')
  assert response.data['nome'] == 'Teste'
  response = client.patch('/api/vendedores/1/', {'nome': 'Teste Atualizado'})
  assert response.status_code == 200
  response = client.get('/api/vendedores/1/')
  assert response.data['nome'] == 'Teste Atualizado'

@pytest.mark.django_db
def test_deletar_vendedor(client):
  client.post('/api/vendedores/', {'nome': 'Teste', 'sobrenome': 'Teste', 'email': 'teste@teste.com'})
  response = client.delete('/api/vendedores/1/')
  assert response.status_code == 204