from django.db import models

class Produtos(models.Model):
  nome = models.CharField(max_length=100, db_index=True)
  preco = models.DecimalField(max_digits=10, decimal_places=2)
  data_cadastro = models.DateField(auto_now_add=True)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.nome

  def delete(self, instance):
    return self.Meta.model.objects.update(is_active=False)

  class Meta:
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'
    db_table = 'produtos'
    ordering = ['nome']
    unique_together = ['nome', 'is_active']