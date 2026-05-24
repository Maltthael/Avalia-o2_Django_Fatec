from django.urls import path
from core.views import login, logout, home, cadastrar_link, listar_link, deletar_link, editar_link


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('cadastrar_link/', cadastrar_link, name='cadastrar_link'),
    path('listar_link/', listar_link, name='listar_link'),
    path('editar_link/<int:id>/', editar_link, name='editar_link'),
    path('deletar_link/<int:id>/', deletar_link, name='deletar_link'),
    path('', home, name='home')
]