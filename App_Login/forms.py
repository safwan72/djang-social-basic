from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CreateNewUser(UserCreationForm):
    email=forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':"Enter Your Email Address"}))
    username=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':"Enter Your Username"}))
    password1=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':"Enter Your Password"}))
    password2=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':"Confirm Your Password"}))
    class Meta:
        model=User
        fields=('email','username','password1','password2')
        
        
        
class EditProfile(forms.ModelForm):
    dob=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=UserProfile
        exclude=('user',)