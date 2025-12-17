from django.shortcuts import render, redirect
from django.http import HttpResponse as hp
from .forms import *
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from services.models import SubCategory, ServiceCategory
from .models import UserService, UserProfile

User = get_user_model()

def index(request):
    return render(request, "users/index.html")



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
    # Get user profile (OneToOne)
    profile = getattr(user, "profile", None)

    # Get services rendered by the user
    user_services = (
        UserService.objects
        .select_related("category", "subcategory")
        .filter(user=user)
    )

    context = {
        "user_obj": user,          # optional, but useful
        "profile": profile,
        "user_services": user_services,
        "user_has_services": user_services.exists(),
    }

    return render(request, "users/profile.html", context)

@login_required
def logmeout(request):
    logout(request)
    messages.success(request,f"You have been logout of of this app")
    return redirect("users:index")


# @login_required
# def add_user_services(request):
#     categories = ServiceCategory.objects.prefetch_related("subcategories")

#     if request.method == "POST":
#         category_id = request.POST.get("category")
#         selected_services = request.POST.getlist("services")

#         category = ServiceCategory.objects.get(id=category_id)

#         for sub_id in selected_services:
#             UserService.objects.get_or_create(
#                 user=request.user,
#                 category=category,
#                 subcategory_id=sub_id
#             )

#         return redirect("users:index")

#     return render(request, "users/userservices.html", {
#         "categories": categories
#     })



@login_required
def add_user_services(request, userid):
    user = get_object_or_404(User, id=userid)
    user_services = (
        UserService.objects
        .select_related("category", "subcategory")
        .filter(user=user)
    )

    categories = ServiceCategory.objects.prefetch_related("subcategories")

    if request.method == "POST":
        category_id = request.POST.get("category")
        selected_services = request.POST.getlist("services")

        category = ServiceCategory.objects.get(id=category_id)

        for sub_id in selected_services:
            UserService.objects.get_or_create(
                user=request.user,
                category=category,
                subcategory_id=sub_id
            )

        return redirect("users:index")
    else:
        form = UserServiceForm()

    context = {
        "form": form,
        "user_obj": user,
        "user_services": user_services,
        "categories": categories
    }

    return render(request, "users/userservices.html", context)


@login_required
def edit_profile(request):
    profile = request.user.profile  # guaranteed by signal

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("users:profile", request.user.id)
    else:
        form = EditProfileForm(instance=profile)

    return render(request, "users/edit_profile.html", {
        "form": form
    })