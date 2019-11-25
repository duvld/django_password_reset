from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import PasswordResetFormWithUsername
from urllib import request
from django.http import HttpResponseRedirect


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class PasswordResetFormWithUsernameView(PasswordResetView):
	form_class = PasswordResetFormWithUsername
	success_url = reverse_lazy('password_reset_done')
	template_name = 'registration/password_reset_form.html'	