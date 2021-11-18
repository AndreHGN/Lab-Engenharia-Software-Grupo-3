from .models import Leilao

leiloes = Leilao.objects.all()
for leilao in leiloes:
    leilao.finalizar()
    leilao.save()