from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView, IndexView

urlpatterns = [
    path('api/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-retrieve-update-delete'),
    path('', IndexView.as_view(), name='index'),
]
