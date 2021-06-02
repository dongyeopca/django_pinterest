from django.db import models
from django.db.models.deletion import SET_NULL
from articleapp.models import Article
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comment')
    writer = models.ForeignKey(User,on_delete=SET_NULL,null=True,related_name="comment")
    content = models.TextField(max_length=200,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

