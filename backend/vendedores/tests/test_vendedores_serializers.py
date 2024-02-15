import pytest
from vendedores.serializers import VendedoresSerializer

@pytest.mark.django_db
def test_valid_vendedores_serializer():
  valid_serializer_data = {
    'nome': 'Teste',
    'sobrenome': 'Teste',
    'email': 'teste@teste',
  }

  serializer = VendedoresSerializer(data=valid_serializer_data)
  assert serializer.is_valid(raise_exception=True)
  assert serializer.validated_data == valid_serializer_data

@pytest.mark.django_db
def test_invalid_vendedores_serializer():
  invalid_serializer_data = {
    'nome': 'Teste',
    'sobrenome': 'Teste',
  }

  serializer = VendedoresSerializer(data=invalid_serializer_data)
  assert not serializer.is_valid(raise_exception=True)