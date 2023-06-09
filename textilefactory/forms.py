from django import forms
from .models import TextileOrder, TextileOrderFile


class TextileOrderForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Файлы', required=False)

    class Meta:
        model = TextileOrder
        fields = ['name', 'description', 'files']
        enctype = 'multipart/form-data'