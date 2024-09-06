from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo',]
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class searchForm(forms.Form):
    query = forms.CharField(label= 'Search', max_length=100)
    