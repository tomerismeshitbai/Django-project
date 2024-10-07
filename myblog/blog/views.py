from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView , UpdateView , DeleteView
from .models import Post , Comment
from .forms import PostForm , CommentForm
from django.urls import reverse_lazy
from django.db.models import Q

class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']
    paginate_by = 5
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
        return Post.objects.all().order_by('-created_at')
    
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    
class DeletePost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
    
    
    
    