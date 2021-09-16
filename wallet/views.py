from django.shortcuts import render
from .models import post
from django.views.generic import (
    ListView
)
from .models import photos

# Create your views here.
class PostListView(ListView):
    template_name = "clone/post_list.html"
    queryset = post.objects.all()
    context_object_name = 'posts'
    
def index(request):
    # imports photos and save it in database
    photo = photos.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'clone/index.html', ctx)

def home(request):
    return render(request, 'clone/home.html')

def upload(request):
    return render(request, 'clone/index.html')

def post_list(request):
    return render(request, 'clone/post_list.html')

def profile(request):
    return render(request, 'clone/profile.html')

def signin(request):
    return render(request, 'login/signin.html')

def signup(request):
    return render(request, 'login/signup.html')




        
