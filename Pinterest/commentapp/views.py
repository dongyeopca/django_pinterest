from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView
from .models import Comment
from .forms import CommentCreateForm
from articleapp.models import Article
from django.contrib.auth.decorators import login_required
from .decorators import comment_ownership_required
@method_decorator(login_required,'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'commentapp/create.html'
    
    def form_valid(self, form):
        temp_form = form.save(commit=False)
        temp_form.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_form.writer = self.request.user
        temp_form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs = {'pk':self.object.article.pk})

@method_decorator(comment_ownership_required,'post')
@method_decorator(comment_ownership_required,'get')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.article.pk})
