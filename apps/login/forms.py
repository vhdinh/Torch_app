from django import forms
from django.forms import ModelForm
from .models import Tweeter

class User_form(ModelForm):
	class Meta:
		model = Tweeter
		fields = ['name', 'username', 'password', 'password2']

class Login_form(ModelForm):
	class Meta:
		model = Tweeter
		fields = ['username', 'password']
