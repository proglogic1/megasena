from django.urls import path
from .views import gerar_combinacoes


urlpatterns = [
    path('', gerar_combinacoes, name='gerar_combinacoes'),
]