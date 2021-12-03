from django.urls import path

from . import views

app_name = 'lote'

urlpatterns = [
  path('', views.lote_list, name='lote_list'),
  path('lote/new/', views.lote_create, name='lote_new'),
  path('lote/edit/<int:pk>/', views.lote_update, name='lote_edit'),
  path('lote/details/<int:pk>/', views.lote_details, name='lote_details'),
  path('lote/delete/<int:pk>/', views.lote_delete, name='lote_delete'),
  path('leilao/details/<int:pk>', views.leilao_details, name='leilao_details'),
  path('leilao/register/<int:pk>', views.create_leilao, name='create_leilao'),
  path('leilao/delete/<int:pk>/', views.leilao_delete, name='leilao_delete'),
  path('leilao/reject/<int:pk>/', views.leilao_reject, name='leilao_reject'),
  path('leilao/cancel/<int:pk>/', views.leilao_cancel, name='leilao_cancel'),
  path('leilao/finalize/<int:pk>/', views.leilao_finalize, name='leilao_finalize'),
  path('lance/register/<int:pk>', views.create_lance, name='create_lance'),
  path('pagamento/verify/<int:pk>', views.verify_pagamento, name='verify_pagamento'),
  path('pagamento/confirm/<int:pk>', views.confirm_pagamento, name='confirm_pagamento'),
]