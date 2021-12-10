from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.fields import IntegerField
from django.shortcuts import render, redirect, get_object_or_404
from django import forms

from lote.models import Lote
from lote.models import Leilao
from lote.models import Lance
from lote.models import Pagamento
from django.contrib.auth.models import User

CHOICES=[('Desempenho','Desempenho'),
        ('Faturamento','Faturamento')]
class FormRelatorio(forms.Form):
    dataInicial = forms.DateField(label='Data Inicial')
    dataFinal = forms.DateField(label='Data Final')
    tipo = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

@user_passes_test(lambda u: u.is_superuser)
def relatorio_interface(request, template_name='relatorio/interface.html'):
    form = FormRelatorio(request.POST or None)
    if form.is_valid():
        dataInicial = form.cleaned_data['dataInicial']
        dataFinal = form.cleaned_data['dataFinal']
        tipo = form.cleaned_data['tipo']
        if tipo == 'Desempenho':
            return redirect('relatorio:relatorio_desempenho', dataInicial=dataInicial, dataFinal=dataFinal)
        else:
            return redirect('relatorio:relatorio_faturamento', dataInicial=dataInicial, dataFinal=dataFinal)
    return render(request, template_name, {'form':form})

@user_passes_test(lambda u: u.is_superuser)
def relatorio_desempenho(request, dataInicial, dataFinal, template_name='relatorio/desempenho.html'):
    leiloesFinalizados = Leilao.objects.filter(finalLeilao__lt = dataFinal)
    leiloesAbertos = Leilao.objects.filter(finalLeilao__gt = dataFinal)
    leiloesIniciados = Leilao.objects.filter(inicioLeilao__gt = dataInicial)
    usuariosNovos = User.objects.filter(date_joined__gt = dataInicial, date_joined__lt = dataFinal)
    nLeiloesFinalizados = len(leiloesFinalizados)
    nLeiloesAbertos = len(leiloesAbertos)
    nLeiloesIniciados = len(leiloesIniciados)
    nUsuariosNovos = len(usuariosNovos)
    return render(request, template_name, {'finalizados':nLeiloesFinalizados, 'abertos':nLeiloesAbertos, 'iniciados':nLeiloesIniciados, 'users': nUsuariosNovos})

@user_passes_test(lambda u: u.is_superuser)
def relatorio_faturamento(request,  dataInicial, dataFinal, template_name='relatorio/faturamento.html'):
    pagamentos = Pagamento.objects.filter(dataDeConfirmacao__gte = dataInicial, dataDeConfirmacao__lte = dataFinal)
    totalArrecadado = 0.00
    labels = []
    economySeries = []

    for pagamento in pagamentos:
        labels.append(str(pagamento.dataDeConfirmacao))
        if (pagamento.lote):
            totalArrecadado += pagamento.valor
        else:
            leilao = get_object_or_404(Leilao, pk=pagamento.leilao)
            totalArrecadado += (pagamento.valor - leilao.maiorLance)
        economySeries.append(totalArrecadado)

    data = economySeries


    return render(request, template_name, {'TotalArrecadado':totalArrecadado, 'labels': labels, 'data': data, "data_inicial": dataInicial, "data_final": dataFinal})
