from django.contrib import admin
from django.urls import path                                                                                             
from .views import(
     PostListView
)
from wallet import views

urlpatterns = [
     path('', views.home, name='home'),
     path('signin', views.signin, name='signin'),
     path('', views.upload, name='upload'),
     path('',PostListView.as_view(), name='post_list'),
    
]