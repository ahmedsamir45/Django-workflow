from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
# Create your views here.

def index(request):

    return render(request,"pages/index.html") 

def about(request):
    if request.method == "POST":
        username = request.POST.get("username")
        text = request.POST.get("text")

        # Validate the form data
        if username and text:
            data = Contact(username=username, text=text)
   
            data.save()
    return render(request,"pages/about.html",{"form":ContactForm}) 