from django.db import models

class Vendedores(models.Model):
  nome = models.CharField(max_length=100)
  sobrenome = models.CharField(max_length=100)
  email = models.EmailField()
  data_cadastro = models.DateField(auto_now_add=True)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.nome} {self.sobrenome}'
    
  class Meta:
    verbose_name = 'Vendedor'
    verbose_name_plural = 'Vendedores'
    db_table = 'vendedores'
    ordering = ['nome']