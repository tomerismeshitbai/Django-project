from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView , UpdateView , DeleteView
from .models import Post , Comment
from .forms import PostForm , CommentForm
from django.urls import reverse_lazy

class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']
    
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    
class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    
class DeletePost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
    
    
    
    