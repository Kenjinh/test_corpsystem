from django.db import models
from vendedores.models import Vendedores

class Paginas(models.Model):
  nome = models.CharField(max_length=255)
  path = models.CharField(max_length=255)

  def __str__(self):
    return self.nome

class Permissoes(models.Model):
  user = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
  pagina = models.ForeignKey(Paginas, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return f'{self.user} - {self.pagina}'

