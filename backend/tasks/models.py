from django.db import models
from datetime  import datetime
from django.contrib.auth.models import User # Importa a tabela de usuários padrão do Django


# Create your models here.

# Tabela principal de Tarefas (Estrutura & ORM
class Task(models.Model):

    # Opções para o campo de Categoria que aparecem na /admin
    OPCOES_CATEGORIA = [
         ('trabalho', 'Trabalho'),
         ('estudos', 'Estudos'),
         ('pessoal', 'Pessoal'),
         ('importante', 'Importante'),
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
        default='trabalho'
    )

    # Controle de prazos (Campo "Dois encontros" da interface)
    data_entrega = models.DateTimeField(default=datetime.now, blank=True)

    # Armazena URLs ou endereços (Campo "Localização / Link")
    link_localizacao = models.URLField(blank=True, null=True)

    # Caixa de marcar importante
    importante = models.BooleanField(default=False)

    # Caixa de marcar tarefa completa (Booleanos: Verdadeiro ou Falso)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True) # Data de criação
    updated_at = models.DateTimeField(auto_now=True) # Última atualização
    

    def __str__(self):
        return self.title
