from django import forms 
from .models import *

class InstaForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'