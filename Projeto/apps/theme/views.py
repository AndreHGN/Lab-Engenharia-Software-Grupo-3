from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from lote.models import Leilao
from lote.models import Lote

def home(request):
    leilao = Leilao.objects.all()
    data = {}
    data['object_list'] = []
    for element in leilao:
        element.liberar()
        lote = get_object_or_404(Lote, nome=element.loteLeilao)
        data['object_list'].append({'id': element.id, 'loteLeilao':element.loteLeilao, 'maiorLance':element.maiorLance, 'valorMinimo': lote.valorMinimo, 'liberado':element.liberado})    
    return render(request, "home.html", data)


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    if request.user.is_superuser:
        leilao = Leilao.objects.all()
    else:
        leilao = Leilao.objects.filter(vendedor=request.user)
    data = {}
    data['leilao_list'] = leilao
    data['user'] = user
    return render(request, 'registration/profile.html', data)