from rest_framework import generics
from .serializers import PermissoesSerializer, PaginasSerializer
from .models import Permissoes, Paginas

class PermissoesList(generics.ListCreateAPIView):
  queryset = Permissoes.objects.all()
  serializer_class = PermissoesSerializer

class PermissoesDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Permissoes.objects.all()
  serializer_class = PermissoesSerializer

class PaginasList(generics.ListCreateAPIView):
  queryset = Paginas.objects.all()
  serializer_class = PaginasSerializer

class PaginasDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Paginas.objects.all()
  serializer_class = PaginasSerializer
