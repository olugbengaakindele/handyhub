from django.shortcuts import render, redirect
from django.http import HttpResponse as hp
from .forms import *
from django.contrib import messages
from django.contrib.auth import logout

def index(request):
    return render(request, "users/base.html")

def register(request):
    form = UserRegisterForm(request.POST or None)

    if request.method == "POST" :
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("users:index")
        else:
            messages.error(request, "There were errors in your form. Please fix them.")

 
    context = {
        "form": form
    }

    return render(request, "users/register.html" , context)


def logmeout(request):
    logout(request)

    return render(request, 'users/logout.html')