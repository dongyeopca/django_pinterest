from django.urls.base import reverse_lazy,reverse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from .forms import ProfileCreationForm
from .models import Profile
from .decorators import profile_ownership_required
# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name= 'target_profile'
    template_name = 'profileapp/create.html'

    def form_valid(self,form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('accountapp:detail',kwargs={'pk':self.object.user.pk})
        
@method_decorator(profile_ownership_required,'get')
@method_decorator(profile_ownership_required,'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('Account:index')
    template_name = 'profileapp/update.html'