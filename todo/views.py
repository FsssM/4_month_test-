from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, View
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

class TaskListView(CreateView, ListView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('task_list')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'
    context_object_name = 'task'

class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect('task_list')
