from django.test import TestCase
from django.urls import reverse
from core.models import LinkModel

class TestListarLinkView(TestCase):
    def test_listar_link_view(self):
        """Testa se a página de listagem carrega e exibe os dados"""
        LinkModel.objects.create(titulo="Link 1", link="http://l1.com", observacao="Obs 1")
        LinkModel.objects.create(titulo="Link 2", link="http://l2.com", observacao="Obs 2")
        
        response = self.client.get(reverse('listar_link'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_link.html')
        
        self.assertEqual(len(response.context['links']), 2)
        self.assertContains(response, "Link 1")
        self.assertContains(response, "Link 2")

    def test_listar_link_vazio(self):
        """Testa se a página carrega mesmo sem nenhum link cadastrado"""
        response = self.client.get(reverse('listar_link'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['links']), 0)
        self.assertContains(response, "Nenhum link cadastrado.")