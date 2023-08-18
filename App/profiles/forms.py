from django import forms
from .models import Profile

#form for editing profile ( firstname, lastname, email and profile picture )
class EditForm(forms.ModelForm):
    firstName = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder' : 'First Name'}))
    lastName  = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder' : 'Last Name'}))
    email     = forms.EmailField(required=False, widget=forms.TextInput(attrs={'placeholder' : 'Email',}))

    class Meta:
        model   = Profile
        fields  = ('profilePicture', 'firstName', 'lastName', 'email')
        widgets = {'profilePicture' : forms.FileInput(attrs={})}