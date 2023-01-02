from django.shortcuts import render,redirect
from .models import Blog
from .forms import Blogdata,contactp
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required (login_url="login")
def data(request):
    if request.method=="GET":
        form=Blogdata()
        return render(request,"home.html",{"form":form})
    else:
        form=Blogdata(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("data")
        else:
            print("error")

@login_required (login_url="login")
def showdata(request):
    blogview=Blog.objects.all()
    return render(request,"showdata.html",{"blogview":blogview})

def delete(request,id):
    a=Blog.objects.get(id=id)
    a.delete()
    return redirect("showdata")

def update(request,id):
    a=Blog.objects.get(id=id)
    if request.method=="GET":
        form=Blogdata(instance=a)
        return render(request,"home.html",{"form":form})
    else:
        form=Blogdata(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print("error")

def contactus(request):
    if request.method=="GET":
        form=contactp()
        return render(request,"contactus.html",{"form":form})
    else:
        form=contactp(request.POST)
        if form.is_valid:
            form.save()
            return redirect("contactus")
        else:
            print("Error")

def signup(request):

    if request.method=="POST":

        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect("signup")
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect("login")

        else:
            messages.info(request,"Password do not match")
    
    return render(request,"signup.html")


def login(request):

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user = auth.authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Invalid Username/Password")
            return redirect('login')
        else:
            auth.login(request,user)
            return redirect('home')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('login')

def ReadMore(request,id):
    a=Blog.objects.get(id=id)
    return render(request,"readmore.html",{"i":a})



        