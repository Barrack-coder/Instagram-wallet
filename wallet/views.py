from django.core.checks import messages
from django.http import request
from django.shortcuts import render,redirect
from django.views.generic import (
    ListView
)
from .models import Post,Profile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User as Users
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class PostListView(ListView):
    template_name = "clone/post_list.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'
    
def index(request):
    post = Post.objects.all()
    return render(request, 'clone/index.html',{'post':post})


def post_list(request):
    if request.method == "POST":
        image= request.FILES['image']
        captions = request.POST['captions']
        post= Post(author=request.user, image=image, captions=captions)
        post.save()
        return redirect("home")
    else:
        return render(request, 'clone/post_list.html')

def profile(request):
    profile = Profile.objects.all()
    if request.method == 'POST':
        username= request.POST['username']
        caption= request.POST['caption']
        profile=profile(username=username,caption=caption)
        profile.save()
            
    else:
        return render(request, 'clone/profile.html')
    
   
    

def signin(request):
    if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Successfully signed in!")
                return redirect(index)
    return render(request, 'login/signin.html')
  
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = Users(username=username, email=email, password=password)
            user.save()
            messages.add_message(request, messages.SUCCESS, "You have successfully registered!")
            return redirect(signin)
        return render(request, 'login/signup.html')     
    
        
    




        
