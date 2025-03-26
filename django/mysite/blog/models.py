from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)  # Título do post
    conteudo = models.TextField()  # Conteúdo do post
    autor = models.CharField(max_length=100)  # Nome do autor
    data_publicacao = models.DateTimeField(auto_now_add=True)  # Data de publicação automática

    def __str__(self):
        return self.titulo  # Representação do modelo em string