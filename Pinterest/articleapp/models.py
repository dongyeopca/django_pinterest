from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from projectapp.models import Project
# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User,on_delete=SET_NULL,related_name='article',null=True)
    project = models.ForeignKey(Project,on_delete=SET_NULL,related_name="article",null=True)
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to="article/",null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title