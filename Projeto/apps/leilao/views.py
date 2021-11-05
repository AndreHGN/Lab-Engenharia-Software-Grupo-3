from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Leilao

class LeilaoForm(ModelForm):
    class Meta:
        model = Leilao
        fields = ['nome', 'descricao', 'estado', 'valorMinimo', 'valorReserva', 'valorMinimoLance', 'inicioLeilao', 'finalLeilao', 'tipoInicial', 'tipoFinal']

def leilao_list(request, template_name='leilao/leilao_list.html'):
    if request.user.is_superuser:
        leilao = Leilao.objects.all()
    else:
        leilao = Leilao.objects.filter(user=request.user)
    data = {}
    data['object_list'] = leilao
    return render(request, template_name, data)
