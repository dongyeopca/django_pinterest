from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView,CreateView,ListView
from django.views.generic.list import MultipleObjectMixin
from .models import Project
from .forms import ProjectForm
from articleapp.models import Article
from subscribeapp.models import Subscription
# Create your views here.
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail',kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView,MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by=20

    def get_context_data(self,**kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,project=project)
        else:
            subscription = None
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView,self).get_context_data(object_list=object_list,subscription=subscription,**kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20
