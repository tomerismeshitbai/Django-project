from django.urls import path 
from .views import UserRegister, EditProfileView , ProfileDetailView


urlpatterns = [
    path('register/', UserRegister.as_view(), name = 'register'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name = 'profile-edit'),
    # path('profile/<int:user_id>/follow/', follow_user, name='follow_user'),
    # path('profile/<int:user_id>/unfollow/', unfollow_user, name='unfollow_user'),
]