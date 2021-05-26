from django.shortcuts import redirect, render
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,UpdateView,DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import DeleteView
from .forms import AccountUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import account_ownership_required

has_ownership = [account_ownership_required,login_required]
def index(request):
    if request.user.is_authenticated:
        return redirect('articleapp:list')
    else:
        return redirect('Account:login')

class AccountCreatView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name= 'Account/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'Account/detail.html'

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