from django.urls import path 
from .views import UserRegister, ProfileView

urlpatterns = [
    path('register/', UserRegister.as_view(), name = 'register'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    
]