from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

class Lote(models.Model):
    vendedor = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    estado = models.CharField(max_length=100)
    valorMinimo = models.FloatField()
    valorReserva = models.FloatField()
    valorMinimoLance = models.FloatField(null=True)
    inicioLeilao = models.DateField(null=True)
    finalLeilao = models.DateField(null=True)
    tipoInicial = models.IntegerField(null=True)
    tipoFinal = models.IntegerField(null=True)
    confirmado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

    def defineTipoInicial(self):
        if (self.valorMinimo <= 1000):
            self.tipoInicial = 1
        elif (self.valorMinimo > 1000 and self.valorMinimo <= 10000):
            self.tipoInicial = 2
        elif (self.valorMinimo > 10000 and self.valorMinimo <= 50000):
            self.tipoInicial = 3
        elif (self.valorMinimo > 50000 and self.valorMinimo <= 100000):
            self.tipoInicial = 4
    
    def confirmar(self):
        self.confirmado = True
        self.save()
    
    def get_absolute_url(self):
        return reverse('lote:lote_edit', kwargs={'pk': self.pk})

class Leilao(models.Model):
    inicioLeilao = models.DateField()
    finalLeilao = models.DateField()
    maiorLance = models.FloatField(null=True)
    loteLeilao = models.CharField(max_length=200)
    vencedor = models.CharField(max_length=200,default="None")
    pagamentoLeilao = models.CharField(max_length=200)
    liberado = models.BooleanField(default=False)
    finalizado = models.BooleanField(default=False)
    confirmaPagamento = models.BooleanField(default=False)
    cancelar = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def defineMaiorLance(self, novoLance):
        if(self.maiorLance):
            if (self.maiorLance < novoLance):
                self.maiorLance = novoLance
                self.save()
        else:
            self.maiorLance = novoLance
            self.save()
    
    def liberar(self):
        hoje = date.today()
        lote = get_object_or_404(Lote, nome=self.loteLeilao)
        if (lote.confirmado and hoje >= self.inicioLeilao and hoje <= self.finalLeilao):
            self.liberado = True
            self.save()
    
    def finalizar(self):
        hoje = date.today()
        if (hoje > self.finalLeilao):
            self.finalizado = True
            self.save()
    
    def solicitarCancelamento(self):
        lote = get_object_or_404(Lote, nome=self.loteLeilao)
        if (lote.confirmado and not self.finalizado and not self.liberado):
            self.cancelar = True
            self.save()
        elif (not lote.confirmado):
            self.delete()

    def get_absolute_url(self):
        return reverse('lote:lote_edit', kwargs={'pk': self.pk})

class Lance(models.Model):
    valor = models.FloatField()
    comprador = models.CharField(max_length=200)
    leilao =  models.IntegerField()

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    valor = models.FloatField()
    efetuador = models.CharField(max_length=200)
    lote = models.IntegerField(default=None)

    def __str__(self):
        return self.nome

    def defineTaxaInicial(self):
        if(self.valor <= 1000):
            taxa = 0.01
        if(self.valor > 1000 and self.valor <= 10000):
            taxa = 0.02
        if(self.valor > 10000 and self.valor <= 50000):
            taxa = 0.03
        if(self.valor > 50000 and self.valor <= 100000):
            taxa = 0.04
        self.valor = self.valor*taxa
        self.save()

    