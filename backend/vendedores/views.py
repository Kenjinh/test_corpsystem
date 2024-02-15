from rest_framework import generics
from .serializers import VendedoresSerializer
from .models import Vendedores

class ListarVendedores(generics.ListCreateAPIView):
  queryset = Vendedores.objects.filter(is_active=True)
  serializer_class = VendedoresSerializer

class DetalharVendedores(generics.RetrieveUpdateDestroyAPIView):
  queryset = Vendedores.objects.filter(is_active=True)
  serializer_class = VendedoresSerializer

