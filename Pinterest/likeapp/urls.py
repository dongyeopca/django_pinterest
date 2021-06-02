from django.urls import path
from .views import LikeArticleView

app_name = "likeapp"

urlpatterns=[
    path('like/<int:pk>',LikeArticleView.as_view(),name="like"),

]