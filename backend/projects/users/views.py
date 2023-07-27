from django.shortcuts import render

# Create your views here.
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeDoneView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetView)
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout

class UserRegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home:homepage')
    def form_valid(self,form):
        response = super().form_valid(form)
        login(self.request,self.object)
        return response
    
class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = '/'
    pass

class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    pass