from django.http.response import HttpResponseForbidden
from .models import Comment

def comment_ownership_required(func):
    def decorated(request,*args,**kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)
    return decorated