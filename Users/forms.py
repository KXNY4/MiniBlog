from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm


USERMODEL = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = USERMODEL
        fields = ['username', 'password']
    

class SignupUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = USERMODEL
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = USERMODEL
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined']
        

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'})),
