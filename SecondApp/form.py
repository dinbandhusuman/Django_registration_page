from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class FormCreation(UserCreationForm):
    password2 = forms.CharField(label='Conform Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username',   'first_name',   'last_name',   'email',]
