from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Register
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth import authenticate, login

# Create your views here.
def page1(request):
    return render(request, "page1.html")

def page2(request):
    return render(request, "page2.html")

def page3(request):
    return render(request, "page3.html")

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('page1.html')
        )
    else:
        login(request, user)
        return HttpResonseRedirect(
            reverse('page1_.html')
        )

def login(request):
    return render(request, "login.html")

def user_reg(request):
    return render(request, "user_reg.html")

def page1_(request):
    return render(request, "page1_.html")