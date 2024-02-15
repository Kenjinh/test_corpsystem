from django.urls import re_path, path
from vendedores.views import *

urlpatterns = [
  path('', ListarVendedores.as_view()),
  re_path(r'^(?P<pk>\d+)?$', DetalharVendedores.as_view()),
]