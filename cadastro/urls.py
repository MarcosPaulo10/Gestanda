from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastros_home, name='cadastros_home'),
    path('produtos/', views.cadastro_produto, name='cadastro_produto'),
    path('clientes/', views.cadastro_cliente, name='cadastro_cliente'),
    path('caixa/', views.cadastro_caixa, name='cadastro_caixa'),
]

