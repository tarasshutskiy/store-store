from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import UserCustom


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter name',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter password',
    }))
    class Meta:
        model = UserCustom
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter First Name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Last Name',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Username',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Confirm Password',
    }))
    class Meta:
        model = UserCustom
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')




class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'readonly': True,
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'readonly': True,
    }))

    class Meta:
        model = UserCustom
        fields = ('image', 'first_name', 'last_name', 'username', 'email')