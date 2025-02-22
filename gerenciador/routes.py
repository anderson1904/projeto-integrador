from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # rotas relativas as campanhas
    path('campanhas/', views.buscar_campanhas, name='campanhas'),
    path('campanhas/editar/<int:campanha_id>/', views.editar_campanha, name='editar_campanha'),
    path('campanhas/criar/', views.criar_campanha, name='criar_campanha'),
    path('campanhas/deletar/<int:campanha_id>/', views.deletar_campanha, name='deletar_campanha'),

    #relativo a Cestas básicas
    path('cestas/', views.buscar_Cestas_Basicas, name='cestas_basicas'),
    path('cestas/criar/', views.criar_cesta_basica, name='criar_Cesta_Basica'),
    path('cestas/editar/<int:cesta_id>/', views.editar_cesta_basica, name='editar_Cesta_Basica'),
    path('cestas/deletar/<int:cesta_id>/', views.deletar_cesta_basica, name='deletar_Cesta_Basica'),
    #relativo a Itens
    path('Itens/', views.buscar_Itens,name='itens'),
    
]