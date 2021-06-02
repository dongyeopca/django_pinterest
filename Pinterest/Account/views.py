from django.shortcuts import redirect, render
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,UpdateView,DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import DeleteView
from django.views.generic.list import MultipleObjectMixin
from .forms import AccountUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import account_ownership_required
from articleapp.models import Article

has_ownership = [account_ownership_required,login_required]

class AccountCreatView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name= 'Account/create.html'


class AccountDetailView(DetailView,MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'Account/detail.html'
    paginate_by = 20
    def get_context_data(self,**kwargs):
        object_list = Article.objects.filter(writer = self.get_object())
        return super(AccountDetailView,self).get_context_data(object_list=object_list,**kwargs)

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('Account:index')
    template_name= 'Account/update.html'

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('Account:login')
    template_name = 'Account/delete.html'