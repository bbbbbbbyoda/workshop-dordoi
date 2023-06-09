from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['username'].label = ''
        self.fields['phone_number'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'Почта'
        self.fields['username'].widget.attrs['placeholder'] = 'Имя пользователя'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Номер телефона (+7)'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторно введите пароль'

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = MyUser
        fields = ("email", "username", "phone_number", "password1", "password2")


class UserAuthenticationForm(forms.Form):
    phone_number = forms.CharField(label='Введите номер телефона',
                                   widget=forms.TextInput(attrs={'placeholder': '+7', 'class': 'form-control'}))

    password = forms.CharField(label='Введите пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ("phone_number", "password")

