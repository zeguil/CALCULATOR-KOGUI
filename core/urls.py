from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('home/', views.calculadora, name='calculadora'),
    path('delete-latest-history/', views.delete_latest_history, name='delete_latest_history'),
]