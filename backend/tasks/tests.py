from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task


class TaskAPITest(APITestCase):

    def setUp(self):
        # Criar usuário
        self.user = User.objects.create_user(
            username='renato',
            password='123456'
        )

        # Fazer login para pegar token
        response = self.client.post(
            reverse('login'),
            {
                'username': 'renato',
                'password': '123456'
            }
        )

        self.access_token = response.data['access']
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

    def test_create_task(self):
        data = {
            "title": "Teste tarefa",
            "description": "Descrição teste",
            "categoria": "pendente"
        }

        response = self.client.post('/api/tasks/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().user, self.user)