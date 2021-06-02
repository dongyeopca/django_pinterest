from django.urls import path
from .views import SubScriptionView,SubscriptionListView
app_name="subscribeapp"

urlpatterns=[
    path('subscribe/',SubScriptionView.as_view(),name="subscribe"),
    path('list/',SubscriptionListView.as_view(),name='list'),
]