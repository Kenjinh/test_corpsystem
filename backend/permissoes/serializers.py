from rest_framework import serializers
from .models import Permissoes, Paginas

class PermissoesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Permissoes
    fields = ['user', 'pagina']

class PaginasSerializer(serializers.ModelSerializer):
  class Meta:
    model = Paginas
    fields = '__all__'