from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Cria o roteador padrão do DRF
router = DefaultRouter()

# Registra o seu ViewSet com o prefixo 'tasks'
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # Inclui todas as rotas geradas automaticamente
    path('', include(router.urls)),
]