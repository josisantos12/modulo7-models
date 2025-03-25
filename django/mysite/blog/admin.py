from django.contrib import admin
from .models import Post

# Registrando o modelo Post no Django Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')  # Exibe estas colunas na interface
    search_fields = ('titulo', 'autor')  # Adiciona campo de pesquisa por título e autor
    list_filter = ('data_publicacao',)  # Permite filtrar por data de publicação