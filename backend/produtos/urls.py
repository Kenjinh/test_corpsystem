from django.urls import path, re_path
from .views import ListarProdutos, DetalharProdutos

urlpatterns = [
  path('', ListarProdutos.as_view()),
  re_path(r'^(?P<pk>\d+)?$', DetalharProdutos.as_view()),
]