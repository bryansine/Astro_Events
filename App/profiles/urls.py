from django.urls import path
from views import profileView, editProfile

app_name = 'profiles'

urlpatterns = [
    path('', profileView, name='profile'),
    path('edit/', editProfile, name='editProfile'),
]