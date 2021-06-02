from django.http.response import HttpResponseRedirect
from articleapp.models import Article
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import RedirectView
from .models import Like
# Create your views here.
@method_decorator(login_required,'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return reverse('articleapp:detail',kwargs={'pk':kwargs['pk']})

    def get(self,*args,**kwargs):
        user= self.request.user
        article = get_object_or_404(Article,pk=kwargs['pk'])
        likecheck = Like.objects.filter(user=user,article=article)

        if likecheck.exists():
            likecheck.delete()
            article.like -=1
            article.save()
            return HttpResponseRedirect(reverse('articleapp:detail',kwargs={'pk':kwargs['pk']}))
        else:
            Like(user=user,article=article).save()
            article.like +=1
            article.save()
        return super(LikeArticleView,self).get(self.request,*args,**kwargs)
