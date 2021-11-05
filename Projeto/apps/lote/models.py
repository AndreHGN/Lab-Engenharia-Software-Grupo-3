from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Lote(models.Model):
    vendedor = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    estado = models.CharField(max_length=100)
    valorMinimo = models.IntegerField()
    valorReserva = models.IntegerField()
    valorMinimoLance = models.IntegerField()
    inicioLeilao = models.DateField()
    finalLeilao = models.DateField()
    tipoInicial = models.IntegerField()
    tipoFinal = models.IntegerField()

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
    
    def get_absolute_url(self):
        return reverse('lote:lote_edit', kwargs={'pk': self.pk})

class Leilao(models.Model):
    inicioLeilao = models.DateField()
    finalLeilao = models.DateField()
    maiorLance = models.CharField(max_length=200)
    loteLeilao = models.CharField(max_length=200)
    pagamentoLeilao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    def defineMaiorLance(self, novoLance):
        if (self.maiorLance.valor < novoLance.valor):
            self.maiorLance = novoLance
    
    def get_absolute_url(self):
        return reverse('lote:lote_edit', kwargs={'pk': self.pk})