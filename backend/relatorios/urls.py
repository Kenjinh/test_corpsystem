from .views import relatorio_vendas
from django.urls import path

urlpatterns = [
  path('relatorio_vendas', relatorio_vendas),
]