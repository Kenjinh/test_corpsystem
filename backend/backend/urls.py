from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clientes/', include('clientes.urls')),
    path('api/vendedores/', include('vendedores.urls')),
    path('api/vendas/', include('vendas.urls')),
    path('api/produtos/', include('produtos.urls')),
    path('api/relatorios/', include('relatorios.urls')),
]
