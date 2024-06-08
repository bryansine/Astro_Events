from django import forms
from profiles.models import PROFILE_TYPE_CHOICES
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))

class SignUpForm(UserCreationForm): #signup form
    email = forms.EmailField(max_length=150, required=True, help_text='Required. Enter a valid email address.')
    role = forms.ChoiceField(
        choices =PROFILE_TYPE_CHOICES,  # Use the predefined choices for role
        required=True,
        widget  =forms.Select(attrs={'class': 'userInputRole'}), # Use a dropdown menu for role selection
        )
    class Meta:
        model  = User
        fields = ('username', 'role', 'email', 'password1', 'password2') # class fields



