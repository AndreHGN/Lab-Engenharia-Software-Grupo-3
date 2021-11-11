from django.urls import path

from . import views

app_name = 'lote'

urlpatterns = [
  path('', views.lote_list, name='lote_list'),
  path('lote/new/', views.lote_create, name='lote_new'),
  path('lote/edit/<int:pk>/', views.lote_update, name='lote_edit'),
  path('lote/delete/<int:pk>/', views.lote_delete, name='lote_delete'),
  path('leilao/details/<int:pk>', views.leilao_details, name='leilao_details'),
  path('leilao/register/<int:pk>', views.create_leilao, name='create_leilao'),
  path('lance/register/<int:pk>', views.create_lance, name='create_lance'),
]