from django.contrib import admin
from django.urls import path                                                                                             
from .views import(
     PostListView
)
from wallet import views
# from photos import views

urlpatterns = [
     
     path('index', views.index, name='index'),
     path('', views.home, name='home'),
     path('signin', views.signin, name='signin'),
     path('', views.upload, name='upload'),
     path('signup', views.signup, name='signup'),
     path('account', views.profile, name='profile'),
     path('post_list',PostListView.as_view(), name='post_list'),
    
     
    
]