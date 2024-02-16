from django.db import models
from vendedores.models import Vendedores

# Create your models here.
class Token(models.Model):
  user = models.OneToOneField(Vendedores, on_delete=models.CASCADE)
  token = models.CharField(max_length=255, blank=True, null=True)
  password = models.CharField(max_length=255)

  def __str__(self):
    return self.token