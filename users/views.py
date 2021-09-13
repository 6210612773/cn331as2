from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth import authenticate,login,logout

from .models import *
# Create your views here.

def indexPage(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/index.html")

def loginPage(request):
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("subject:index"))
        else:
            return render(request, "users/login.html", {
                "message ": "invalid credential."
            })
    return render(request, "users/login.html")

def logoutPage(request):
    logout(request)

    return render(request, "users/login.html", {
        "message": "logged out."
    })