from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('dash', views.dash, name="dash"),
    path('complain', views.complain, name="complain"),
    path('send', views.send, name='send'),
]
