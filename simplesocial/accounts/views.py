from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm

    # same as the get_absolute_url in the models
    # for where to go after jobs succesfully done
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
