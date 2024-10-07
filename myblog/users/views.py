from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.urls import reverse_lazy


class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class ProfileView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user