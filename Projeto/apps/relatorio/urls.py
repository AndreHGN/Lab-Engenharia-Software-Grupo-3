from django.urls import path

from . import views

app_name = 'relatorio'

urlpatterns = [
  path('', views.lote_list, name='lote_list'),
  path('/new/', views.lote_create, name='lote_new'),
] 