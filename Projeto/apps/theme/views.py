from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from lote.models import Leilao

def home(request):
    leilao = Leilao.objects.all()
    data = {}
    data['object_list'] = leilao
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
    return render(request, 'registration/profile.html', {'user':user})