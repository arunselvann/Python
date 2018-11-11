from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('User does not exist')
        if not user.check_password(password):
            raise forms.ValidationError('Incorrect Password')
        if not user.is_active:
            raise forms.ValidationError('User is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class SignUp_F(forms.Form):
    First_Name = forms.CharField()
    Last_Name = forms.CharField()


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username','email','password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email has been registered already')
        return email