from .models import Subscription
from projectapp.models import Project
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.generic.base import RedirectView
from articleapp.models import Article

# Create your views here.
@method_decorator(login_required,'get')
class SubScriptionView(RedirectView):
    def get_redirect_url(self):
        return reverse('projectapp:detail',kwargs={'pk':self.request.GET.get('project_pk')})

    def get(self,request,*args,**kwargs):
        project = get_object_or_404(Project,pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user,project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user,project=project).save()
        return super(SubScriptionView,self).get(request,*args,**kwargs)

@method_decorator(login_required,'get')
class SubscriptionListView(ListView):
    model = Project
    template_name = 'subscribeapp/list.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        print(projects)
        article_list = Article.objects.filter(project__in=projects)
        print(article_list)
        return article_list