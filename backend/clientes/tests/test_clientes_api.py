import pytest
#Test cliente API Create get update delete

@pytest.mark.django_db
def test_get_client_api(client):
  response = client.get('/api/clientes/')
  assert response.status_code == 200


@pytest.mark.django_db
def test_create_client_api(client):
  response = client.post('/api/clientes/', {
    'nome': 'Teste', 
    'sobrenome': 'Teste', 
    'email': 'teste@teste.com', 
    'telefone': '123456789', 
    'cpf': '12345678901', 
    'endereco': 'Rua Teste',
    'cidade': 'Teste',
    'estado': 'SP',
    'cep': '12345678',
    'data_nascimento': '2022-01-01',
  })
  assert response.status_code == 201
  assert response.data['nome'] == 'Teste'
  assert response.data['sobrenome'] == 'Teste'
  assert response.data['email'] == 'teste@teste.com'
  assert response.data['cpf'] == '12345678901'
  assert response.data['data_nascimento'] == '2022-01-01'
  assert response.data['cep'] == '12345678'
  response = client.get('/api/clientes/1/')
  assert response.status_code == 200


@pytest.mark.django_db
def test_update_client_api(client):
  response = client.post('/api/clientes/', {
    'nome': 'Teste1', 
    'sobrenome': 'Teste', 
    'email': 'teste@teste.com', 
    'telefone': '123456789', 
    'cpf': '12345678901', 
    'endereco': 'Rua Teste',
    'cidade': 'Teste',
    'estado': 'SP',
    'cep': '12345678',
    'data_nascimento': '2022-01-01',
  })
  assert response.status_code == 201

  response = client.put('/api/clientes/1/', {
    'nome': 'Teste2', 
    'sobrenome': 'Teste', 
    'email': 'teste@teste.com', 
    'telefone': '123456789', 
    'cpf': '12345678901', 
    'endereco': 'Rua Teste',
    'cidade': 'Teste',
    'estado': 'SP',
    'cep': '12345678',
    'data_nascimento': '2022-01-01',
  })
  assert response.status_code == 200
  assert response.data['nome'] == 'Teste2'


@pytest.mark.django_db
def test_delete_client_api(client):
  response = client.post('/api/clientes/', {
    'nome': 'Teste1', 
    'sobrenome': 'Teste', 
    'email': 'teste@teste.com', 
    'telefone': '123456789', 
    'cpf': '12345678901', 
    'endereco': 'Rua Teste',
    'cidade': 'Teste',
    'estado': 'SP',
    'cep': '12345678',
    'data_nascimento': '2022-01-01', 
  })
  assert response.status_code == 201
  response = client.delete('/api/clientes/1/')
  assert response.status_code == 204


  
