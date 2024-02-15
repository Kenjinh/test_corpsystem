from rest_framework import generics
from .serializers import ProdutosSerializer
from .models import Produtos

class ListarProdutos(generics.ListCreateAPIView):
  queryset = Produtos.objects.filter(is_active=True)
  serializer_class = ProdutosSerializer

class DetalharProdutos(generics.RetrieveUpdateDestroyAPIView):
  queryset = Produtos.objects.filter(is_active=True)
  serializer_class = ProdutosSerializer