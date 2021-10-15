from django.urls import path

from . import views

app_name = 'lote'

urlpatterns = [
  path('', views.lote_list, name='lote_list'),
  path('new/', views.lote_create, name='lote_new'),
  path('edit/<int:pk>/', views.lote_update, name='lote_edit'),
  path('delete/<int:pk>/', views.lote_delete, name='lote_delete'),
]