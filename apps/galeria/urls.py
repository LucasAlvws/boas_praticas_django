
from django.urls import path, include
from .views import index, imagem, buscar, nova_img, editar_img, deletar_img

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:id>',imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-img', nova_img, name="nova-img"),
    path('editar-img', editar_img, name="editar-img"),
    path('deletar-img', deletar_img, name="deletar-img"),
]