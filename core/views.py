from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Operacao
import operator

def registrar_usuario(request):
    """view para registrar um novo usuário."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('calculadora')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})

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
    return render(request, 'registration/login.html', {'form': form})

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

    # últimas 5 operações do usuário logado
    operacoes_recentes = Operacao.objects.filter(usuario=request.user)[:5]
    contexto['historico'] = operacoes_recentes
    
    return render(request, 'core/calculadora.html', contexto)