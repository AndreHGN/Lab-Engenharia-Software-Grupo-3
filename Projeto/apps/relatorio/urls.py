from django.urls import path, register_converter
from datetime import datetime
from . import views

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

app_name = 'relatorio'

urlpatterns = [
  path('', views.relatorio_interface, name='relatorio_interface'),
  path('desempenho/<yyyy:dataInicial>/<yyyy:dataFinal>/', views.relatorio_desempenho, name='relatorio_desempenho'),
  path('faturamento/<yyyy:dataInicial>/<yyyy:dataFinal>/', views.relatorio_faturamento, name='relatorio_faturamento'),
] 