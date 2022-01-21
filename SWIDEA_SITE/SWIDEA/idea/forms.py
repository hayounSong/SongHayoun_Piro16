from dataclasses import field
from django import forms
from .models import Devtool, Idea

class IdeaForm(forms.ModelForm):

    class Meta:
        model=Idea
        
        fields=('__all__')


class DevForm(forms.ModelForm):

    class Meta:
        model=Devtool

        fields=('__all__')