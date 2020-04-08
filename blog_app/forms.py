from .models import Comment, Post
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
      #  model.author= 'zyarra'

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content', 'image')
        # image = forms.ImageField(required=False)