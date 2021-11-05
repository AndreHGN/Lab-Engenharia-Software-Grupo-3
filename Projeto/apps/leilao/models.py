from django.db import models
from django.urls import reverse


class Leilao(models.Model):
    inicioLeilao = models.DateField()
    finalLeilao = models.DateField()
    maiorLance = models.CharField()
    loteLeilao = models.CharField()
    pagamentoLeilao = models.CharField()

    def __str__(self):
        return self.nome

    def defineMaiorLance(self, novoLance):
        if (self.maiorLance.valor < novoLance.valor):
            self.maiorLance = novoLance
    
    def get_absolute_url(self):
        return reverse('lote:lote_edit', kwargs={'pk': self.pk})