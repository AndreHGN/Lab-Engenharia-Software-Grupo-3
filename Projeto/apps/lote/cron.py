from .models import Leilao


def verificarFinalizacao():
    leiloes = Leilao.objects.all()
    for leilao in leiloes:
        leilao.finalizar()
        leilao.save()