from django import forms
from .models import Event

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'poster', 'venue', 'date', 'size', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date'       :forms.TextInput(attrs={'type':'datetime-local'}),
        }

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'poster', 'venue', 'date', 'size', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date'       :forms.TextInput(attrs={'type':'datetime-local'}),
        }


