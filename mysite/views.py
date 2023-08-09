from django.shortcuts import render

# Create your views here.

def home(request):
    print("Home View")
    return render(request,'mysite/home.html')

def about(request):
    print("About View")
    return render(request,'mysite/about.html')