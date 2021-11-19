from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.fields import IntegerField
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm, forms

from .models import Lote
from .models import Leilao
from .models import Lance
from .models import Pagamento

class LoteFormVendedor(ModelForm):
    class Meta:
        model = Lote
        fields = ['nome', 'descricao', 'estado', 'valorMinimo', 'valorReserva']

class LoteFormLeiloeiro(ModelForm):
    class Meta:
        model = Lote
        fields = ['valorMinimoLance', 'inicioLeilao', 'finalLeilao']

class LoteFormUpdateLeiloeiro(ModelForm):
    class Meta:
        model = Lote
        fields = ['nome', 'descricao', 'estado', 'valorMinimo', 'valorReserva', 'valorMinimoLance', 'inicioLeilao', 'finalLeilao']

class LanceForm(ModelForm):
    class Meta:
        model = Lance
        fields = ['valor']
        leilao = IntegerField()

    def clean_valor(self):
        leilao = get_object_or_404(Leilao, pk=self.leilao)
        lote = get_object_or_404(Lote, nome=leilao.loteLeilao)
        valor = self.cleaned_data['valor']
        print(leilao.loteLeilao)
        if leilao.maiorLance:
            if valor - leilao.maiorLance < lote.valorMinimoLance:
                raise forms.ValidationError("Valor de lance menor que o mínimo")
        else:
            if valor - lote.valorMinimo < lote.valorMinimoLance:
                raise forms.ValidationError("Valor de lance menor que o mínimo")
        return valor

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
        return redirect('lote:lote_details', pk=lote.id)
    return render(request, template_name, {'form':form})

@login_required
def lote_update(request, pk, template_name='lote/lote_form.html'):
    if request.user.is_superuser:
        lote = get_object_or_404(Lote, pk=pk)
        form = LoteFormUpdateLeiloeiro(request.POST or None, instance=lote)
    else:
        lote = get_object_or_404(Lote, pk=pk, vendedor=request.user)
        form = LoteFormVendedor(request.POST or None, instance=lote)
    if form.is_valid():
        lote.defineTipoInicial()
        lote.pendente = False
        form.save()
        return redirect('lote:lote_details', pk=lote.id)
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

@login_required
def lote_details(request, pk, template_name='lote/lote_details.html'):
    lote = get_object_or_404(Lote, pk=pk)
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
        pagamento = Pagamento.objects.create(valor=lote.valorMinimo, efetuador=lote.vendedor, lote=lote.id)
        pagamento.defineTaxaInicial()
        return redirect('lote:lote_list')
    return render(request, template_name, {'form':form, 'lote':lote})

@user_passes_test(lambda u: u.is_superuser)
def leilao_delete(request, pk, template_name='leilao/leilao_confirm_delete.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    if request.method=='POST':
        leilao.delete()
        return redirect('profile')
    return render(request, template_name, {'object':leilao})

@user_passes_test(lambda u: u.is_superuser)
def leilao_reject(request, pk, template_name='leilao/leilao_reject_delete.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    if request.method=='POST':
        leilao.cancelar = False
        leilao.save()
        return redirect('profile')
    return render(request, template_name, {'object':leilao})

@user_passes_test(lambda u: u.is_superuser)
def leilao_finalize(request, pk, template_name='leilao/leilao_finalize.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    if request.method=='POST':
        leilao.finalizar(True)
        return redirect('/')
    return render(request, template_name, {'object':leilao})

@login_required
def leilao_cancel(request, pk, template_name='leilao/leilao_request_delete.html'):
    leilao = get_object_or_404(Leilao, pk=pk)
    if request.method=='POST':
        leilao.cancelar = True
        leilao.save()
        return redirect('profile')
    return render(request, template_name, {'object':leilao})

@login_required
def create_lance(request, pk, template_name='lance/create_lance.html'):
    form = LanceForm(request.POST or None)
    form.leilao = pk
    leilao = get_object_or_404(Leilao, pk=pk)
    lote = get_object_or_404(Lote, nome=leilao.loteLeilao)
    if (leilao.maiorLance):
        atual = leilao.maiorLance
        minimo = leilao.maiorLance + lote.valorMinimoLance
    else:
        atual = lote.valorMinimo
        minimo = lote.valorMinimo + lote.valorMinimoLance
    if form.is_valid():
        lance = form.save(commit=False)
        lance.comprador = request.user
        lance.leilao = pk
        lance.save()
        leilao.defineMaiorLance(lance.valor)
        return redirect('lote:leilao_details', pk=pk)
    return render(request, template_name, {'form':form, 'atual':atual, 'minimo':minimo})

@user_passes_test(lambda u: u.is_superuser)
def verify_pagamento(request, pk, template_name='leilao/verify_pagamento.html'):
    pagamento = get_object_or_404(Pagamento, lote=pk)
    lote = get_object_or_404(Lote, pk=pk)
    if request.method=='POST':
        lote.confirmar()
        return redirect('lote:lote_list')
    return render(request, template_name, {'pagamento':pagamento, 'lote':lote})

@user_passes_test(lambda u: u.is_superuser)
def confirm_pagamento(request, pk, template_name='leilao/confirm_pagamento.html'):
    pagamento = get_object_or_404(Pagamento, leilao=pk)
    leilao = get_object_or_404(Leilao, pk=pk)
    if request.method=='POST':
        leilao.confirmaPagamento = True
        leilao.save()
        return redirect('profile')
    return render(request, template_name, {'pagamento':pagamento, 'leilao':leilao})