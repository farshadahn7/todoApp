from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo
from .forms import TodoForm


class TaskListView(LoginRequiredMixin, ListView):
    model = Todo
    queryset = Todo.objects.all()
    context_object_name = 'tasks'
    template_name = 'todo.html'

    def get_queryset(self, **kwargs):
        return Todo.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo.html'
    success_url = reverse_lazy('todo:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class TaskStatusUpdateView(LoginRequiredMixin, View):
    model = Todo
    template_name = 'todo.html'
    success_url = reverse_lazy('todo:home')

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Todo, pk=self.kwargs['pk'])
        if task.status == 'in_progress':
            task.status = 'done'
        else:
            task.status = 'in_progress'
        task.save()
        return redirect('todo:home')


class TaskDeleteView(LoginRequiredMixin, View):
    model = Todo
    template_name = 'todo.html'
    success_url = reverse_lazy('todo:home')

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Todo, pk=self.kwargs['pk'])
        task.delete()
        return redirect('todo:home')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('todo:home')
    context_object_name = 'task'
