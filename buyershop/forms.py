from django import forms
from django.contrib.auth import get_user_model
MyUser = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'phone_number']



