
from django.contrib import messages
from .forms import PetitionSignupForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def petition_signup(request):
    if request.method == 'POST':
        form = PetitionSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing the petition!')
            return redirect('home')
    else:
        form = PetitionSignupForm()
    
    return render(request, 'events/petition_signup.html', {'form': form})

@login_required
def petition_signup(request):
    form = PetitionSignupForm()  
    
    if request.method == 'POST':
        form = PetitionSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing the petition!')
            return redirect('home')  

    return render(request, 'petition_signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
