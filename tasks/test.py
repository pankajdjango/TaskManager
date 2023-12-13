from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'description': 'Testing', 'status': 'Pending'}
        self.task = Task.objects.create(**self.task_data)
        self.url_list_create = reverse('task-list-create')
        self.url_retrieve_update_delete = reverse('task-retrieve-update-delete', args=[self.task.id])

    def test_get_all_tasks(self):
        response = self.client.get(self.url_list_create)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_task(self):
        response = self.client.get(self.url_retrieve_update_delete)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        response = self.client.post(self.url_list_create, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description', 'status': 'Completed'}
        response = self.client.put(self.url_retrieve_update_delete, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(self.url_retrieve_update_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
