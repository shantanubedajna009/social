from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):


    class Meta():

        fields = ('username', 'email', 'password1', 'password2')

        # get the current model of whoever is accesing the website
        model = get_user_model()


    # this whole part is just for changing the labels of the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # just changing the form labels here
        self.fields['username'].label = 'Diaplay Name'
        self.fields['email'].label = 'Email Address'
