from django.urls import re_path, path
from clientes.views import *

urlpatterns = [
  path('', ListarClientes.as_view()),
  re_path(r'^(?P<pk>\d+)?/$', DetalharCliente.as_view()),
]