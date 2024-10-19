from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Cliente
from .forms import RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirecionar para o dashboard
    else:
        form = LoginForm()
    return render(request, 'clientes/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'clientes/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def home(request):
    return render(request, 'clientes/home.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('lista_clientes')  # Redirecionar para a lista de clientes
    else:
        form = RegistroForm()
    return render(request, 'clientes/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_clientes')  # Redirecionar para a lista de clientes
    else:
        form = LoginForm()
    return render(request, 'clientes/login.html', {'form': form})

