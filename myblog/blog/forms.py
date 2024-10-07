from django import forms
from .models import Post , Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','author')
        
        widgets = {
           'title': forms.TextInput(attrs = {'class': 'form-control'}),
           'content': forms.Textarea(attrs = {'class': 'form-control'}),
           'author': forms.Select(attrs = {'class': 'form-select'}),
        }
            
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add a comment...'}),
        }