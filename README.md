# 🖥️ Backend — Sistema de Gestão de Tarefas Acadêmicas

## 📚 Sobre o Projeto

O Sistema de Gestão de Tarefas Acadêmicas foi desenvolvido para resolver uma problemática real enfrentada por estudantes e professores:

- Dificuldade em organizar tarefas e prazos  
- Falta de acompanhamento de atividades concluídas e pendentes  
- Ausência de centralização das informações acadêmicas  

Este backend robusto foi construído com Django, simulando um cenário real de mercado, oferecendo uma API segura, estruturada e escalável para integração com um frontend em React.

---

## 🚀 Tecnologias e Recursos Utilizados

- 🐍 Django  
- 🔗 Django REST Framework (API REST)  
- 🗄️ ORM do Django  
- 💾 Banco de Dados SQLite  
- 🔐 Autenticação JWT  
- 🛡️ Sistema de Permissões  
- 🔎 Filtros de consulta  
- 📄 Paginação de resultados  
- 📘 Documentação interativa com Swagger  

---

## 🔧 Funcionalidades da API

- Autenticação e geração de token JWT  
- CRUD completo de tarefas  
- Controle de acesso por usuário  
- Filtros para organização das tarefas  
- Paginação para melhor desempenho  
- Documentação acessível para testes e integração  

---

## ▶️ Como Executar o Projeto

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações
python manage.py migrate

# Executar o servidor
python manage.py runserver
