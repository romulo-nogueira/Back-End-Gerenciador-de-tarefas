from django.db import models
from datetime  import datetime
from django.contrib.auth.models import User # Importa a tabela de usuários padrão do Django


# Create your models here.

# Tabela principal de Tarefas (Estrutura & ORM
class Task(models.Model):

    # Opções para o campo de Categoria que aparecem na /admin
    OPCOES_CATEGORIA = [
         ('concluido', 'Concluído'),
         ('pendente', 'Pendente'),
    ]

    # Vincula a tarefa a um usuário (Dono da tarefa)
    # CASCADE > Se o usuario for deletado, as tarefas também serão deletadas
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True, blank=True)

    title = models.CharField(max_length=255) # Título da tarefa
    description = models.TextField(blank=True, null=True) # Descrição da tarefa

    # Campo de escolha usando a lista definida acima
    categoria = models.CharField (
        max_length=50, 
        choices=OPCOES_CATEGORIA,
        default='concluido'
    )

    # Representa quando a tarefa deve começar
    data_inicio = models.DateTimeField(default=datetime.now, verbose_name="Data de Início")

    # Representa o prazo final
    data_entrega = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Date de Término")
    

    def __str__(self):
        return self.title
