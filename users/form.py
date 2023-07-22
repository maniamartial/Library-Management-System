#from users.models import Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from datetime import datetime
from .models import Member


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'national_id']