from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    # class Meta:
    #     model = User
    #     fields = ('username', 'password1', 'password2')
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
    #         'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
    #         'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
    #     }
        