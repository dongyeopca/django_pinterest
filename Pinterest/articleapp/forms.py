from django import forms
from .models import Article
from projectapp.models import Project

class ArticleCreateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class':'editable','style':'text-align:left;'})
    )
    project = forms.ModelChoiceField(queryset=Project.objects.all(),required=False)
    class Meta:
        model = Article
        fields = ['title','image','project','content']
