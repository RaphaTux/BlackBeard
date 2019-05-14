from django.urls import path
from .views import clientes
from .views import novo_cliente
from .views import atualiza_cliente
from .views import deleta_cliente


urlpatterns = [
       path( 'list/',clientes, name="clientes"),
       path( 'novoCliente/',novo_cliente,name="novo_cliente"),
       path( 'atualizaCliente/<int:id>',atualiza_cliente,name='atualiza_cliente'),
       path( 'deletaCliente/<int:id>',deleta_cliente,name='deleta_cliente')
]
