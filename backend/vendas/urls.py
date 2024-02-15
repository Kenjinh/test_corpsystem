from django.urls import path, re_path
from .views import ListarVendas, DetalharVenda, ListarItensVenda, DetalharItemVenda

urlpatterns = [
  path('', ListarVendas.as_view()),
  re_path(r'^(?P<pk>\d+)/', DetalharVenda.as_view()),
  path('itens/', ListarItensVenda.as_view()),
  re_path(r'^itens/(?P<pk>\d+)/', DetalharItemVenda.as_view()),
]