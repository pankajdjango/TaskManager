from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.views.generic import TemplateView


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class IndexView(TemplateView):
    template_name = 'index.html'
