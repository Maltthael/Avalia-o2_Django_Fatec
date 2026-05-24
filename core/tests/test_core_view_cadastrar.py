from django.test import TestCase
from django.urls import reverse
from core.models import LinkModel
from django.contrib.auth.models import User

class TestCadastrarLinkView(TestCase):
    def setUp(self):
        self.url = reverse('cadastrar_link')

    def test_cadastrar_link_get(self):
        """Testa o acesso à página de cadastro (cobre o else)"""
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'forms.html')

    def test_cadastrar_link_post_valido(self):
        user = User.objects.create_user(username='teste', password='123')
        self.client.login(username='teste', password='123')

        dados = {'titulo': 'Google', 'link': 'https://google.com', 'observacao': 'Obs'}
        response = self.client.post(self.url, dados)
    
        self.assertRedirects(response, reverse('index'))

    def test_cadastrar_link_post_invalido(self):
        """Testa o envio com dados inválidos (cobre o else do is_valid)"""
        dados = {'titulo': '', 'link': '', 'observacao': ''}
        response = self.client.post(self.url, dados)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forms.html')
        self.assertEqual(LinkModel.objects.count(), 0)