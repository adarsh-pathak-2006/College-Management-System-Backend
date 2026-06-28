from django import forms
from administration.models import User
from django.forms import ModelForm


class RegisterForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    username=forms.CharField()
    email=forms.EmailField()
    role=forms.ChoiceField(choices=User.ROLE_CHOICES)
    password=forms.CharField(widget=forms.PasswordInput())
    rep_password=forms.CharField(widget=forms.PasswordInput())

