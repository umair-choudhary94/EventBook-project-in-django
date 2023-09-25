from django.db import models
from django.forms import fields
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(),
    first_name = forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField()
    password2=forms.CharField()
    role = forms.ChoiceField(choices=[('-1', 'Select What You Are?'),('Participant', 'Participant'), ('Offerer', 'Offerer')])

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email','role')
       
   