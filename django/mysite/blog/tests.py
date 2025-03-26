
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            titulo="Título de Teste",
            conteudo="Conteúdo de Teste",
            autor="Josiane"
        )

    def test_post_criacao(self):
        self.assertEqual(self.post.titulo, "Título de Teste")
        self.assertEqual(self.post.conteudo, "Conteúdo de Teste")
        self.assertEqual(self.post.autor, "Josiane")
        self.assertIsNotNone(self.post.data_publicacao)  # Confirma que a data foi gerada

    def test_repr_string(self):
        self.assertEqual(str(self.post), "Título de Teste")  # Testa a representação em string