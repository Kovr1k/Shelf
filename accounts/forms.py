from typing import Any
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, ModelChoiceField, Select, DateInput, CharField, IntegerField, EmailField, EmailInput, PasswordInput, ImageField, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import UserData

class AllowedChar:
    AllowedChar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
    code = 'eng'

    def __init__(self, message=None):
        self.message = message if message else 'Должны присутствовать только символы латинского алфавита, цифры или символы "_", "-"'

    def __call__(self, value, *args, **kwds):
        if not (set(value) <= (set(self.AllowedChar))):
            raise forms.ValidationError(self.message, code=self.code)

class registerForm(UserCreationForm):
    username = CharField(max_length=32, 
                         min_length=4,
                         widget = TextInput(attrs={'class': 'form-control'}), 
                         error_messages={
                            'max_lenght': 'Сликшом длинный логин',
                            'min_length': 'Слишком короткий логин'
                         },
                         validators=[
                             AllowedChar(),
                         ]
                         )
    first_name = CharField(max_length=64, 
                           widget = TextInput(attrs={'class': 'form-control'}), 
                           )
    email = EmailField(max_length=128, 
                       widget = EmailInput(attrs={'class': 'form-control'})
                       )
    password1 = CharField(widget = PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(validators=[
                             AllowedChar(),
                         ], 
                         widget = PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'email',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("Логин уже занят!")
        return username
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if get_user_model().objects.filter(first_name=first_name).exists():
            raise forms.ValidationError("Псевдоним уже занят!")
        return first_name
    
class updateUserDataForm(ModelForm):
    class Meta:
        model = UserData
        fields = ['AboutMe', 'photo', 'bookGenres', 'VK', 'Telegram', 'Instagram']

        widgets = {
            "AboutMe": Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 15vh;',
            }),
            "VK": TextInput(attrs={
                'class': 'form-control',
                'style': ''
            }),
            "Telegram": TextInput(attrs={
                'class': 'form-control',
                'style': ''
            }),
            "Instagram": TextInput(attrs={
                'class': 'form-control',
                'style': ''
            }),
        }