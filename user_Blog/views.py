from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'user_blog/home.html')

def blogPage(request):
    allposts=Post.objects.all()
    return render(request,'user_blog/blogPage.html',{'allposts':allposts})

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    return render(request,'user_blog/blogPost.html',{'post':post})


def handleSignUp(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        pwd=request.POST.get('pwd','')

        myuser=User.objects.create_user(username=username,password=pwd)
        myuser.save()
        return redirect('home')

def handleLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        pwd=request.POST['pwd']

        user=authenticate(username=username,password=pwd)
        login(request,user)
        return redirect('blogPage')
    

def handleLogout(request):
    logout(request)
    return redirect('home')

def addPost(request):
    if request.method=='POST':
        title=request.POST.get('title','')
        content=request.POST.get('content','')
        author=request.POST.get('author','')
        slug=request.POST.get('slug','')
        timestamp=request.POST.get('timestamp','')

        post = Post(title=title, content=content, author=author, slug=slug,timestamp=timestamp)
        post.save()
    return render(request,'user_blog/addPost.html')