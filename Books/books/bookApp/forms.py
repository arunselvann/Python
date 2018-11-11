from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['First_name', 'Last_name', 'Email', 'Password']
        widgets = {
            'First_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'Last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'Password': forms.PasswordInput(attrs={'placeholder': 'New password'}),
        }

class LoginForm(forms.Form):
    Email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    Password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))