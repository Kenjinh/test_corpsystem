from rest_framework import generics
from .serializers import ClienteSerializer
from .models import Cliente

class ListarClientes(generics.ListCreateAPIView):
  queryset = Cliente.objects.filter(is_active=True)
  serializer_class = ClienteSerializer

class DetalharCliente(generics.RetrieveUpdateDestroyAPIView):
  queryset = Cliente.objects.filter(is_active=True)
  serializer_class = ClienteSerializer