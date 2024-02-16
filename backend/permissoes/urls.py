from django.urls import path, re_path
from .views import PermissoesList, PermissoesDetail, PaginasList, PaginasDetail

urlpatterns = [
  path('', PermissoesList.as_view()),
  re_path(r'^(?P<pk>\d+)?$', PermissoesDetail.as_view()),
  path('pagina', PaginasList.as_view()),
  re_path(r'pagina/(?P<pk>\d+)?$', PaginasDetail.as_view()),
]