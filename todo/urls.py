from django.urls import path
from .views import TaskListView, TaskDetailView, ToggleTaskStatusView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/toggle/', ToggleTaskStatusView.as_view(), name='toggle_task'),
]