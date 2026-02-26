from django.contrib import admin
from .models import Task
# from django.db import models
# Register your models here.

# Configuração da interface administrativa na listagem de tarefas no paineil
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Colunas que aparecerão na listagem de tarefas no painel
    list_display = ('title', 'user', 'categoria')

    # Filtros laterais para facilitar a navegação
    list_filter = ('categoria', 'user')

    # Campos que podem ser usados na barra de busca
    search_fields = ('title', 'description', 'categoria')

