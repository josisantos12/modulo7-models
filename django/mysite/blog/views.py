from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# filepath: c:\Users\josia\projeto\templates\mysite\mysite\urls.py
from django.contrib import admin
from django.urls import path
from blog import views  # Corrija a importação para o módulo correto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Exemplo de rota para a função index
]