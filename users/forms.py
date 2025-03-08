
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    school = forms.CharField(max_length=255)
    year = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'school', 'year']



class Userform(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']