from rest_framework import generics, views
from rest_framework import status
from rest_framework.response import Response
from .serializers import VendasSerializer, ItensVendasSerializer
from .models import Vendas, ItensVendas

from ipdb import set_trace

class ListarVendas(views.APIView):
  def get(self, request):
    filters = {}
    data = self.request.query_params.get('data')
    data_inicial = self.request.query_params.get('data_inicial')
    data_final = self.request.query_params.get('data_final')
    vendedor = self.request.query_params.get('vendedor')
    cliente = self.request.query_params.get('cliente')
    if data:
      filters['data'] = data
    if data_inicial:
      filters['data__gte'] = data_inicial
    if data_final:
      filters['data__lte'] = data_final
    if vendedor:
      filters['vendedor__nome__icontains'] = vendedor
    if cliente:
      filters['cliente__nome__icontains'] = cliente
    
    vendas = Vendas.objects.filter(is_active=True, **filters)
    serializer = VendasSerializer(vendas, many=True)
    return Response(serializer.data)

  def post(self, request):
    venda = VendasSerializer(data=request.data.get('venda'))
    if venda.is_valid():
      venda.save()
      produtos = request.data.get('produtos')
      for item in produtos:
        item['venda'] = venda.data.get('id')
        item_venda = ItensVendasSerializer(data=item)
        if item_venda.is_valid():
          item_venda.save()
        else:
          venda.delete()
          return Response(item_venda.errors, status=status.HTTP_400_BAD_REQUEST)
      
      return Response(status=status.HTTP_201_CREATED)
    return Response(venda.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalharVenda(views.APIView):
  def get(self, request, pk):
    venda = Vendas.objects.get(pk=pk)
    serializer = VendasSerializer(venda)
    return Response(serializer.data)

  def put(self, request, pk):
    venda = Vendas.objects.get(pk=pk)
    request.data.pop('produtos')
    serializer = VendasSerializer(venda, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    venda = Vendas.objects.get(pk=pk)
    if venda:
      venda.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)

class ListarItensVenda(generics.ListCreateAPIView):
  queryset = ItensVendas.objects.filter(is_active=True)
  serializer_class = ItensVendasSerializer

class DetalharItemVenda(views.APIView):
  def get(self, request, pk):
    item = ItensVendas.objects.get(pk=pk)
    serializer = ItensVendasSerializer(item)
    return Response(serializer.data)
  
  def put(self, request, pk):
    item = ItensVendas.objects.get(pk=pk)
    serializer = ItensVendasSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    item = ItensVendas.objects.get(pk=pk)
    if item:
      item.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)
  