from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('home/', views.calculadora, name='calculadora'),
    path('delete-latest/', views.delete_latest, name='delete_latest'),
]