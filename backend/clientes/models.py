from django.db import models

# Create your models here.

class Cliente(models.Model):
  nome = models.CharField(max_length=100)
  sobrenome = models.CharField(max_length=100)
  cpf = models.CharField(max_length=11, unique=True, db_index=True)
  email = models.EmailField()
  telefone = models.CharField(max_length=20)
  endereco = models.CharField(max_length=200)
  cidade = models.CharField(max_length=100)
  estado = models.CharField(max_length=2)
  cep = models.CharField(max_length=8)
  data_nascimento = models.DateField()
  data_cadastro = models.DateField(auto_now_add=True)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.nome} {self.sobrenome}'

  class Meta:
    verbose_name = 'Cliente'
    verbose_name_plural = 'Clientes'
    db_table = 'clientes'
    ordering = ['nome']