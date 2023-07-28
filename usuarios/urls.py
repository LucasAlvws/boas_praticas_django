
from django.urls import path, include
from .views import login, cadastro, logout


urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout')
]