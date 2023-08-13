from django import forms
from .models import Event

class EventCreationForm(forms.ModelForm):
    class Meta:
        model   = Event
        fields  = ['title', 'description', 'poster', 'venue', 'date', 'size', 'price']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }

class EventEditForm(forms.ModelForm):
    class Meta:
        model   = Event
        fields  = ['title', 'description', 'poster', 'venue', 'date', 'size', 'price']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }


