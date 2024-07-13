from django.shortcuts import render
from .models import Login
from .forms import LoginForm
# Create your views here.

def index(request):
    x = {
        "name":"ali",
        "age": 20,
    }
    return render(request,"pages/index.html",x) 

def about(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Validate the form data
        if username and password:
            data = Login(username=username, password=password)
   
            data.save()
    return render(request,"pages/about.html",{"form":LoginForm}) 