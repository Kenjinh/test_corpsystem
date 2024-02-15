from django.db import models
from clientes.models import Cliente
from vendedores.models import Vendedores
from produtos.models import Produtos

class Vendas(models.Model):
  STATUS_CHOICES = (
    ('pendente', 'Pendente'),
    ('pago', 'Pago'),
    ('cancelado', 'Cancelado'),
  )
  PAGAMENTOS_CHOICES = (
    ('cartao', 'Cartão'),
    ('dinheiro', 'Dinheiro'),
    ('cheque', 'Cheque'),
    ('boleto', 'Boleto'),
    ('pix', 'Pix'),
  )
  cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
  data = models.DateField()
  total = models.DecimalField(max_digits=10, decimal_places=2)
  pagamento = models.CharField(max_length=20, choices=PAGAMENTOS_CHOICES)
  observacoes = models.TextField(null=True, blank=True)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
  data_cadastro = models.DateField(auto_now_add=True)
  is_active = models.BooleanField(default=True)
  
  class Meta:
    verbose_name = 'Venda'
    verbose_name_plural = 'Vendas'
    db_table = 'vendas'
    ordering = ['data']


class ItensVendas(models.Model):
  venda = models.ForeignKey(Vendas, on_delete=models.CASCADE, related_name='produtos')
  produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
  quantidade = models.PositiveIntegerField()
  data_cadastro = models.DateField(auto_now_add=True)
  is_active = models.BooleanField(default=True)

  class Meta:
    verbose_name = 'Item de Venda'
    verbose_name_plural = 'Itens de Vendas'
    db_table = 'itens_vendas'
    ordering = ['id']
    unique_together = ['venda', 'produto', 'is_active']