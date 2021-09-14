from django.shortcuts import render
from .models import post
from django.views.generic import (
    ListView
)

# Create your views here.
class PostListView(ListView):
    template_name = "clone/post_list.html"
    queryset = post.objects.all()
    context_object_name = 'posts'

def home(request):
    return render(request, 'clone/home.html')

def upload(request):
    return render(request, 'clone/index.html')

def signin(request):
    return render(request, 'login/signin.html')
        
