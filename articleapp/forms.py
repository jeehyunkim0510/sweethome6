from django import forms
from django.forms import ModelForm

from articleapp.models import NewArticle


class NewArticleCreationForm(ModelForm):
    class Meta:
        model = NewArticle
        fields = ['image', 'content', 'created_at']
        widgets = {
            'created_at': forms.SelectDateWidget()
        }