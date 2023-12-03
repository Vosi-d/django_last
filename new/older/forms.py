from .models import Arka
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArkaForm(ModelForm):
    class Meta:
        model = Arka
        fields = ['title', 'trailer', 'full_text', 'when']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of post'
            }),
            'trailer': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Trailer of post'
            }),
            'when': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            }),

        }