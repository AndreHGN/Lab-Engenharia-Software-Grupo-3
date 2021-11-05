from django.urls import path

from . import views

app_name = 'lote'

urlpatterns = [
  path('', views.leilao_list, name='leilao_list'),
]