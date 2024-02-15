import pytest
from clientes.serializers import ClienteSerializer

@pytest.mark.django_db
def test_valid_cliente_serializer():
    valid_serializer_data = {
        'nome': 'Teste',
        'sobrenome': 'Teste',
        'email': 'teste@teste',
        'telefone': '123456789',
        'cpf': '12345678901',
        'data_nascimento': '2022-01-01',
        'endereco': 'Rua Teste',
        'cidade': 'Teste',
        'estado': 'SP',
        'cep': '12345678'
    }

    serializer = ClienteSerializer(data=valid_serializer_data)
    assert serializer.is_valid(raise_exception=True)
    assert serializer.validated_data == valid_serializer_data

@pytest.mark.django_db
def test_invalid_cliente_serializer():
    invalid_serializer_data = {
        'nome': 'Teste',
        'sobrenome': 'Teste',
        'email': 'teste@teste',
        'cpf': '12345678901',
        'data_nascimento': '2022-01-01',
        'endereco': 'Rua Teste',
        'cidade': 'Teste',
        'estado': 'SP',
        'cep': '12345678'
    }

    serializer = ClienteSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid(raise_exception=True)
