from django.test import TestCase
from django.urls import reverse
from core.models import LinkModel

class TestDeletarLinkView(TestCase):
    def setUp(self):
        self.link = LinkModel.objects.create(
            titulo="Link de Teste", 
            link="http://teste.com", 
            observacao="Teste"
        )
        self.url = reverse('deletar_link', args=[self.link.id])

    def test_deletar_link_com_post(self):
        """Testa se o POST realmente remove o objeto do banco de dados"""
        response = self.client.post(self.url)
        
        self.assertRedirects(response, reverse('listar_link'))
        
        self.assertEqual(LinkModel.objects.count(), 0)

    def test_deletar_link_com_get(self):
        """Testa se o GET não apaga o link e apenas redireciona"""
        self.assertEqual(LinkModel.objects.count(), 1)
        
        response = self.client.get(self.url)
        
        self.assertRedirects(response, reverse('listar_link'))
        
        self.assertEqual(LinkModel.objects.count(), 1)

    def test_deletar_link_inexistente_retorna_404(self):
        """Testa se tentar deletar um ID que não existe dá erro 404"""
        response = self.client.post(reverse('deletar_link', args=[9999]))
        self.assertEqual(response.status_code, 404)