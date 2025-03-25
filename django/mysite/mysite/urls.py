from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à página inicial!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Inclui as URLs do app blog
    path('', home, name='home'),  # Adiciona uma rota para o caminho vazio
]