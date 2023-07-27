
from django.urls import path, include
from .views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:id>',imagem, name='imagem')
]