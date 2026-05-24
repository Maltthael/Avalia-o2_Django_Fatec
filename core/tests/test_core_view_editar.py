from django.test import TestCase
from django.urls import reverse
from core.models import LinkModel

class TestEditarLinkView(TestCase):
    def setUp(self):
        self.link = LinkModel.objects.create(
            titulo="Teste", 
            link="http://teste.com", 
            observacao="Obs"
        )
        self.url = reverse('editar_link', args=[self.link.id])

    def test_editar_link_get_acesso(self):
        """Testa se a página de edição carrega corretamente (cobre o else do POST)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forms.html')

    def test_editar_link_post_valido(self):
        """Testa a edição com sucesso (cobre o if form.is_valid())"""
        dados = {
            'titulo': 'Novo Titulo',
            'link': 'http://novo.com',
            'observacao': 'Nova Obs'
        }
        
        response = self.client.post(self.url, dados)
        self.assertRedirects(response, reverse('listar_link'))
        
        self.link.refresh_from_db()
        self.assertEqual(self.link.titulo, 'Novo Titulo')

    def test_editar_link_post_invalido(self):
        """Testa o formulário inválido (cobre o else do form.is_valid())"""
        dados = {'titulo': '', 'link': '', 'observacao': ''}
        response = self.client.post(self.url, dados)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forms.html')

    def test_editar_link_404(self):
        """Testa o acesso a um ID inexistente (cobre o get_object_or_404)"""
        response = self.client.get(reverse('editar_link', args=[9999]))
        self.assertEqual(response.status_code, 404)