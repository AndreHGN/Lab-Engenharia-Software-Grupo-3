from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Lote
from .models import Leilao

class LoteForm(ModelForm):
    class Meta:
        model = Lote
        fields = ['nome', 'descricao', 'estado', 'valorMinimo', 'valorReserva', 'valorMinimoLance', 'inicioLeilao', 'finalLeilao', 'tipoInicial', 'tipoFinal']

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
    form = LoteForm(request.POST or None)
    if form.is_valid():
        lote = form.save(commit=False)
        lote.vendedor = request.user
        lote.save()
        return redirect('lote:lote_list')
    return render(request, template_name, {'form':form})

@login_required
def lote_update(request, pk, template_name='lote/lote_form.html'):
    if request.user.is_superuser:
        lote = get_object_or_404(Lote, pk=pk)
    else:
        lote = get_object_or_404(Lote, pk=pk, user=request.user)
    form = LoteForm(request.POST or None, instance=lote)
    if form.is_valid():
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

def leilao_details(request, nomeLote, template_name='leilao/leilao_details.html'):
    lote = get_object_or_404(Lote, nome=nomeLote)
    leilao = get_object_or_404(Leilao, loteLeilao=nomeLote)
    return render(request, template_name, {'lote':lote, 'leilao': leilao})