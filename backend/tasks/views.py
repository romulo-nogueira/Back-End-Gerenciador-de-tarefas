from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from .pagination import StandardResultsSetPagination

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    pagination_class = StandardResultsSetPagination
    
    permission_classes = [IsAuthenticated] 

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtros exatos (ex:/api/tasks/?categoria=pendente)
    filterset_fields = ['categoria', 'data_inicio', 'data_entrega'] 
    
    # Busca textual
    search_fields = ['title', 'description'] 
    
    # Ordenação 

    ordering_fields = ['data_inicio', 'data_entrega']
    ordering = ['-data_inicio'] # Padrão: mostra as mais recentes primeiro

    def get_queryset(self):
        """
        O usuário só pode ver suas próprias tarefas.
        Sobrescrevemos a query padrão para filtrar pelo usuário logado na requisição.
        """
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        criar uma nova tarefa (POST), salva automaticamente vinculando 
        ao usuário que fez a requisição.
        """
        serializer.save(user=self.request.user)