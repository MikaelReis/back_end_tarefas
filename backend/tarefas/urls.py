from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('login/', obtain_auth_token, name='api_token_auth'),
]