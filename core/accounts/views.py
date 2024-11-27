from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView


class TaskLoginView(LoginView):
    model = CustomUser
    redirect_authenticated_user = True
    template_name = 'registration/login.html'


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo:home')
        else:
            return render(request, 'registration/signup.html')


class TaskLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')
