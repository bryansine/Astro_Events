from profiles.models import Profile
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, EmailAuthenticationForm
from django.shortcuts import redirect, render, redirect


def home(request):
    return render(request, 'home.html')

def login_view(request): # login_view function
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user) # login user
                return redirect('home:home')  
    else:
        form = EmailAuthenticationForm()
    return render(request, 'registration/login.html', { 'form': form })
    

def signUpView(request): # signup function
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the User instance

            # Create a Profile instance and associate it with the user
            profile = Profile.objects.create(user=user)  # Create the profile instance
            role = form.cleaned_data['role']
            email = form.cleaned_data['email']
            profile.role = role
            profile.email = email
            profile.save()

            # Log the user in
            login(request, user)

            return redirect('home:home')  # 
    else:
        form = SignUpForm()

    return render(request, 'authentication/signup.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('home')