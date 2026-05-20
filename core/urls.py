from django.urls import path
from core.views import login, logout, home, cadastrar_link, listar_link


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('cadastrar_link/', cadastrar_link, name='cadastrar_link'),
    path('listar_link/', listar_link, name='listar_link'),
    path('', home, name='home')
]