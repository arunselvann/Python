from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.post
        fields = ['title', 'content', 'image', 'draft', 'publish']