from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    maiorLance = models.FloatField(null=True)
    loteLeilao = models.CharField(max_length=200)
    pagamentoLeilao = models.CharField(max_length=200)

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
    taxaDeComissao = models.FloatField(default=None)
    

    def __str__(self):
        return self.nome

    def defineTaxa(self):
        if(self.valor <= 1000):
            self.taxaDeComissão = 0.01
        if(self.valor > 1000 and self.valor <= 10000):
            self.taxaDeComissão = 0.02
        if(self.valor > 10000 and self.valor <= 50000):
            self.taxaDeComissão = 0.03
        if(self.valor > 50000 and self.valor <= 100000):
            self.taxaDeComissão = 0.04
    