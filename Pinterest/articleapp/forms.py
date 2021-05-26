from Pinterest.articleapp.models import Article
from django import forms
from .models import Article

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','image','content']
