
from django.contrib import messages
from .forms import PetitionSignupForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def petition_signup(request):
    form = PetitionSignupForm()  # Initialize an empty form for petition signup
    
    # Process form submission if it's a POST request
    if request.method == 'POST':
        form = PetitionSignupForm(request.POST)
        # Validate the form data
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Thank you for signing the petition!')  # Display success message
            return redirect('home')  # Redirect to the home page after successful form submission
    
    # Render the petition signup form
    return render(request, 'petition_signup.html', {'form': form})

# View function for the home page
def home(request):
    return render(request, 'home.html')

# View function for the about page
def about(request):
    return render(request, 'about.html')









# @login_required
# def petition_signup(request):
#     if request.method == 'POST':
#         form = PetitionSignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Thank you for signing the petition!')
#             return redirect('home')
#     else:
#         form = PetitionSignupForm()
    
#     return render(request, 'events/petition_signup.html', {'form': form})
