from django.urls import path
from core.views import login, logout, home, cadastrar


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('', home, name='home')
]