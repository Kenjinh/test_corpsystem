from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from openpyxl import Workbook
from vendas.models import Vendas

def relatorio_vendas(request):
    filters = {}
    if request.GET.get('data_inicial'):
      filters['data__gte'] = request.GET.get('data_inicial')
    elif request.GET.get('data_final'):
      filters['data__lte'] = request.GET.get('data_final')
    elif request.GET.get('data') :
      filters['data'] = request.GET.get('data')
    elif request.GET.get('vendedor') :
      filters['vendedor'] = request.GET.get('vendedor')
    elif request.GET.get('cliente') :
      filters['cliente'] = request.GET.get('cliente')
    vendas = Vendas.objects.filter(**filters)
    if request.GET.get('method') == 'pdf':
      response = HttpResponse(content_type='application/pdf')
      response['Content-Disposition'] = 'attachment; filename="relatorio_vendas.pdf"'

      doc = SimpleDocTemplate(response, pagesize=letter)
      elements = []

      data = [['ID', 'Data', 'Total', 'Pagamento', 'Observações', 'Status', 'Cliente', 'Vendedor']]

      for venda in vendas:
          data.append([
              venda.id,
              venda.data,
              f'R${venda.total:.2f}',
              venda.pagamento,
              venda.observacoes,
              venda.status,
              venda.cliente,
              venda.vendedor,
          ])

      table = Table(data)
      table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

      elements.append(table)
      doc.build(elements)
      return response
    elif request.GET.get('method') == 'excel':
      response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
      response['Content-Disposition'] = 'attachment; filename="relatorio_vendas.xlsx"'

      wb = Workbook()
      ws = wb.active
      ws.append(['ID', 'Data', 'Total', 'Pagamento', 'Observações', 'Status', 'Cliente', 'Vendedor'])

      for venda in vendas:
          ws.append([
              venda.id,
              venda.data,
              f'R${venda.total:.2f}',
              venda.pagamento,
              venda.observacoes,
              venda.status,
              venda.cliente.__str__(),
              venda.vendedor.__str__(),
          ])

      wb.save(response)
      return response