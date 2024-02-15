from rest_framework import serializers
from .models import Vendas, ItensVendas


class ItensVendasSerializer(serializers.ModelSerializer):
  produto_name = serializers.CharField(source='produto.__str__', read_only=True)
  class Meta:
    model = ItensVendas
    fields = ['id','produto', 'produto_name', 'quantidade', 'venda']
  
  def create(self, validated_data):
    return self.Meta.model.objects.create(**validated_data)

  def update(self, instance, validated_data):
    for attr, value in validated_data.items():
      setattr(instance, attr, value)
    instance.save()
    return instance
  
  def delete(self, instance):
    return self.Meta.model.objects.update(is_active=False)

class VendasSerializer(serializers.ModelSerializer):
  produtos = ItensVendasSerializer(many=True, read_only=True)
  cliente_name = serializers.CharField(source='cliente.__str__', read_only=True)
  vendedor_name = serializers.CharField(source='vendedor.__str__', read_only=True)
  class Meta:
    model = Vendas
    fields = '__all__'

  def __str__(self):
    return self.id
  
  def create(self, validated_data):
    return self.Meta.model.objects.create(**validated_data)

  def update(self, instance, validated_data):
    for attr, value in validated_data.items():
      setattr(instance, attr, value)
    instance.save()
    return instance
  
  def delete(self, instance):
    return self.Meta.model.objects.update(is_active=False)

