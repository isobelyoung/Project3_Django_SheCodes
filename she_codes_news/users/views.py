from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic.detail import DetailView
from django.contrib import messages

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class AccountView(generic.DetailView):
    model = CustomUser
    template_name = 'users/Account.html'

class ChangeAccountView(UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy('news:index')
    template_name = 'users/changeAccount.html'

class AuthorView(generic.DetailView):
    template_name="users/authorStories.html"
    model = CustomUser
    context_object_name = "author"

class ChangePassword(UpdateView):
    form_class = PasswordChangeForm
    template_name = 'users/password_change_form.html'