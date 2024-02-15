from rest_framework import serializers
from produtos.models import Produtos

class ProdutosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Produtos
    fields = '__all__'

  def __str__(self):
    return self.nome

  def create(self, validated_data):
    return self.Meta.model.objects.create(**validated_data)

  def update(self, instance, validated_data):
    for attr, value in validated_data.items():
      setattr(instance, attr, value)
    instance.save()
    return instance
  
  def delete(self, instance):
    return self.Meta.model.objects.update(is_active=False)