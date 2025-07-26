from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import Operacao
from .forms import CustomUserCreationForm

import operator

def home(request):
    return render(request, 'home/home.html')

def registrar_usuario(request):
    """view para registrar um novo usuário."""
    if request.method == 'POST':

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
    context = {}
    
    if request.method == 'POST':
        num1_str = request.POST.get('num1')
        num2_str = request.POST.get('num2')
        operator_symbol = request.POST.get('operador') # The form still sends 'operador'

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        try:
            num1_float = float(num1_str)
            num2_float = float(num2_str)
            
            if operator_symbol == '/' and num2_float == 0:
                context['error'] = "Error: Division by zero is not allowed."
            else:
                result = operations[operator_symbol](num1_float, num2_float)
                context['result'] = result
                
                # Create the Operation record in the database
                Operacao.objects.create(
                    usuario=request.user,
                    parametros=f"{num1_str} {operator_symbol} {num2_str}",
                    resultado=str(result)
                )

        except (ValueError, TypeError):
            context['error'] = "Error: Please enter valid numbers."
        except KeyError:
            context['error'] = "Error: Invalid operator."

    # Fetch the 5 most recent operations for the logged-in user
    recent_operations = Operacao.objects.filter(usuario=request.user)[:5]
    context['history'] = recent_operations
    
    return render(request, 'home/calculator.html', context)

@login_required
def delete_latest(request):
    if request.method == 'POST':
        try:
            latest_operation = Operacao.objects.filter(usuario=request.user).order_by('-dt_inclusao').first()
            if latest_operation:
                latest_operation.delete()

        except Operacao.DoesNotExist:
            pass
        
    return redirect('calculadora')
