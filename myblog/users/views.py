from django.shortcuts import render , redirect , get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from django.urls import reverse_lazy
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Profile , Follow


class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class EditProfileView(generic.UpdateView):
    form_class = ProfileForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user.profile

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile.html' 
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('users:profile', user_id=user_id)
    
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('users:profile', user_id=user_id)
