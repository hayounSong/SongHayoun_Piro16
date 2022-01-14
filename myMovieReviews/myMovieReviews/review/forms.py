from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        image = forms.ImageField()
        fields=('__all__')
        
# from django.forms import ModelForm
# from .models import Post

# class FileUploadForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'imgfile', 'content']