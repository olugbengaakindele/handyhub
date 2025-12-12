from django.shortcuts import render, redirect
from django.http import HttpResponse as hp
from .forms import *
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



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
            return redirect("users:register")

 
    context = {
        "form": form
    }

    return render(request, "users/register.html" , context)

@login_required
def profile(request, userid):

    user = get_object_or_404(User, id=userid)

    # If you created a UserProfile model
    profile_user = getattr(user, "profile", None)

    context = {
        "user_obj": user,
        "profile_user": profile_user,
    }

    return render(request, "users/profile.html", context)

@login_required
def logmeout(request):
    logout(request)
    messages.success(request,f"You have been logout of of this app")
    return redirect("users:index")
