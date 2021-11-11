from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Lote
from .models import Leilao
from .models import Lance

class LoteFormVendedor(ModelForm):
    class Meta:
        model = Lote
        fields = ['nome', 'descricao', 'estado', 'valorMinimo', 'valorReserva']

class LoteFormLeiloeiro(ModelForm):
    class Meta:
        model = Lote
        fields = ['valorMinimoLance', 'inicioLeilao', 'finalLeilao']

class LanceForm(ModelForm):
    class Meta:
        model = Lance
        fields = ['valor']

@login_required
def lote_list(request, template_name='lote/lote_list.html'):
    if request.user.is_superuser:
        lote = Lote.objects.all()
    else:
        lote = Lote.objects.filter(vendedor=request.user)
    data = {}
    data['object_list'] = lote
    return render(request, template_name, data)

@login_required
def lote_create(request, template_name='lote/lote_form.html'):
    form = LoteFormVendedor(request.POST or None)
    if form.is_valid():
        lote = form.save(commit=False)
        lote.vendedor = request.user
        lote.defineTipoInicial()
        lote.tipoFinal = 0
        lote.save()
        return redirect('lote:lote_list')
    return render(request, template_name, {'form':form})

@login_required
def lote_update(request, pk, template_name='lote/lote_form.html'):
    if request.user.is_superuser:
        lote = get_object_or_404(Lote, pk=pk)
    else:
        lote = get_object_or_404(Lote, pk=pk, user=request.user)
    form = LoteFormVendedor(request.POST or None, instance=lote)
    if form.is_valid():
        lote.defineTipoInicial()
        form.save()
        return redirect('lote:lote_list')
    return render(request, template_name, {'form':form})

@login_required
def lote_delete(request, pk, template_name='lote/lote_confirm_delete.html'):
    if request.user.is_superuser:
        lote = get_object_or_404(Lote, pk=pk)
    else:
        lote = get_object_or_404(Lote, pk=pk, user=request.user)
    if request.method=='POST':
        lote.delete()
        return redirect('lote:lote_list')
    return render(request, template_name, {'object':lote})

def leilao_details(request, pk, template_name='leilao/leilao_details.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    lote = get_object_or_404(Lote, nome=leilao.loteLeilao)
    return render(request, template_name, {'lote':lote, 'leilao': leilao})

@user_passes_test(lambda u: u.is_superuser)
def create_leilao(request, pk, template_name='leilao/create_leilao.html'):
    lote = get_object_or_404(Lote, pk=pk)
    form = LoteFormLeiloeiro(request.POST or None, instance=lote)
    if form.is_valid():
        form.save()
        leilao = Leilao.objects.create(inicioLeilao = lote.inicioLeilao, finalLeilao = lote.finalLeilao, loteLeilao = lote.nome)
        return redirect('lote:lote_list')
    return render(request, template_name, {'form':form})

@login_required
def create_lance(request, pk, template_name='lance/create_lance.html'):
    form = LanceForm(request.POST or None)
    leilao = get_object_or_404(Leilao, pk=pk)
    lote = get_object_or_404(Lote, nome=leilao.loteLeilao)
    if form.is_valid():
        lance = form.save(commit=False)
        lance.comprador = request.user
        lance.leilao = pk
        if (leilao.maiorLance):
            if (lance.valor >= leilao.maiorLance + lote.valorMinimoLance):
                lance.save()
                leilao.defineMaiorLance(lance.valor)
        else:
            if (lance.valor >= lote.valorMinimo + lote.valorMinimoLance):
                lance.save()
                leilao.defineMaiorLance(lance.valor)
        return redirect('lote:leilao_details', pk=pk)
    return render(request, template_name, {'form':form})