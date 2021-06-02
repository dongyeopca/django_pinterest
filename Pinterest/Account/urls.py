from os import name
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'Account'

urlpatterns = [
    path('create/',views.AccountCreatView.as_view(),name='create'),
    path('login/',LoginView.as_view(template_name="Account/login.html"),name='login'),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('detail/<int:pk>',views.AccountDetailView.as_view(),name='detail'),
    path('update/<int:pk>',views.AccountUpdateView.as_view(),name="update"),
    path('delete/<int:pk>',views.AccountDeleteView.as_view(),name='delete'),
]