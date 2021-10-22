from django.test import TestCase
from lote.models import Lote

class LoteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Lote.objects.create(vendedor='banana', nome='lote_de_teste', descricao='descricao_teste', estado='estado_teste', valorMinimo=100, valorReserva=200, valorMinimoLance=5, inicioLeilao='2021-01-10', finalLeilao='2021-01-15', tipoInicial=1, tipoFinal=1)


    def test_vendedor_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('vendedor').verbose_name
        self.assertEquals(field_label, 'vendedor')

    def test_nome_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')
    
    def test_descricao_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('descricao').verbose_name
        self.assertEquals(field_label, 'descricao')
        
    def test_estado_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('estado').verbose_name
        self.assertEquals(field_label, 'estado')
    
    def test_valor_minimo_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('valorMinimo').verbose_name
        self.assertEquals(field_label, 'valorMinimo')
    
    def test_valor_reserva_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('valorReserva').verbose_name
        self.assertEquals(field_label, 'valorReserva')
    
    def test_valor_minimo_lance_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('valorMinimoLance').verbose_name
        self.assertEquals(field_label, 'valorMinimoLance')
    
    def test_inicio_leilao_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('inicioLeilao').verbose_name
        self.assertEquals(field_label, 'inicioLeilao')
    
    def test_final_leilao_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('finalLeilao').verbose_name
        self.assertEquals(field_label, 'finalLeilao')
 
    def test_tipo_inicial_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('tipoInicial').verbose_name
        self.assertEquals(field_label, 'tipoInicial')
 
    def test_tipo_final_label(self):
        lote = Lote.objects.get(nome='lote_de_teste')
        field_label = lote._meta.get_field('tipoFinal').verbose_name
        self.assertEquals(field_label, 'tipoFinal')
