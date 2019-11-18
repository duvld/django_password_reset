from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import PasswordResetFormWithUsername


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class PasswordResetFormWithUsernameView(generic.CreateView):
	form_class = PasswordResetFormWithUsername
	success_url = reverse_lazy('login')
	template_name = 'signup.html'
	