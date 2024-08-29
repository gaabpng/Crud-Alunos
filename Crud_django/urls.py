from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #rota, view responsavel, nome de referência
    path('', views.home, name='home'), #rota inicial
    path('adicionar', views.adicionar_aluno, name='adicionar_aluno'), 
    path('adicionar_erro', views.adicionar_aluno_erro, name="adicionar_aluno_erro"),
    path('listar', views.listar_aluno, name='listar_aluno'),
    path('deletar/<int:id_aluno>/', views.deletar_aluno, name = 'deletar_aluno'),
    path('editar/<int:id_aluno>/', views.editar_aluno, name='editar_aluno'),
    path('test', views.teste, name='teste'),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)