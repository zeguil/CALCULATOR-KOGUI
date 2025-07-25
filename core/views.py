from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Operacao
import operator

from .forms import CustomUserCreationForm

def registrar_usuario(request):
    """view para registrar um novo usuário."""
    if request.method == 'POST':
        # Usa o formulário customizado
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('calculadora')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'user/register.html', {'form': form})


def login_usuario(request):
    """view para login do usuário."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('calculadora')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def logout_usuario(request):
    """view para logout."""
    logout(request)
    return redirect('login')

@login_required
def calculadora(request):
    """view principal da calculadora e do histórico."""
    contexto = {}
    
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        op = request.POST.get('operador')

        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        try:
            num1_float = float(num1)
            num2_float = float(num2)
            
            if op == '/' and num2_float == 0:
                contexto['erro'] = "Erro: Divisão por zero não é permitida."
            else:
                resultado = ops[op](num1_float, num2_float)
                contexto['resultado'] = resultado
                
                Operacao.objects.create(
                    usuario=request.user,
                    parametros=f"{num1} {op} {num2}",
                    resultado=str(resultado)
                )

        except (ValueError, TypeError):
            contexto['erro'] = "Erro: Por favor, insira números válidos."
        except KeyError:
            contexto['erro'] = "Erro: Operador inválido."

    operacoes_recentes = Operacao.objects.filter(usuario=request.user)[:5]
    contexto['historico'] = operacoes_recentes
    
    return render(request, 'home/index.html', contexto)