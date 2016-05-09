from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class User_form(UserCreationForm):
    fields = ('__all__')
