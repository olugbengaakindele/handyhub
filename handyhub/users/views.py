from django.shortcuts import render, redirect
from django.http import HttpResponse as hp
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from services.models import SubCategory, ServiceCategory
from .models import UserService, UserProfile
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

# home page
def index(request):
    return render(request, "users/index.html")

# about us
def about(request):
    """
    Renders the About Us page for HandymenHub.
    """
    return render(request, "users/about.html")

# register 
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


# custom login view
def custom_login_view(request):
    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")  # email field in the form
            password = form.cleaned_data.get("password")

            # Look up user by email
            try:
                user_obj = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "User not found or profile does not exist.")
                return render(request, "users/login.html", {"form": form})

            # Authenticate using the username of that user
            user = authenticate(username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")  # or your homepage
            else:
                messages.error(request, "Incorrect password.")
        else:
            messages.error(request, "Please enter a valid email and password.")
    else:
        form = EmailLoginForm()

    return render(request, "users/login.html", {"form": form})

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


# this add services to a user
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

        # ✅ NOTHING SELECTED → just go back to profile
        if not category_id or not selected_services:
            return redirect("users:profile", request.user.id)

        category = get_object_or_404(ServiceCategory, id=category_id)

        for sub_id in selected_services:
            UserService.objects.get_or_create(
                user=request.user,
                category=category,
                subcategory_id=sub_id
            )

        return redirect("users:profile", request.user.id)

    context = {
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


#  this is the delete confirmation view

@login_required
def delete_user_service(request, service_id):
    try:
        # Try to get the service belonging to the current user
        service = UserService.objects.get(id=service_id, user=request.user)
    except UserService.DoesNotExist:
        messages.error(request, "You do not have permission to delete this service.")
        # Redirect safely to their service list
        return redirect("users:userservice", userid=request.user.id)

    if request.method == "POST":
        service.delete()
        messages.success(request, "Service removed successfully.")
        return redirect("users:userservice", userid=request.user.id)

    # Optional: if you want a confirmation page
    return render(request, "users/delete_user_service.html", {"service": service})


@login_required
def edit_profile_picture(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfilePictureForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            return redirect("users:profile" , request.user.id)
        else:
            messages.error(
                request,
                "There was an error updating your profile picture. Please try again."
            )

    else:
        form = ProfilePictureForm(instance=profile)

    return render( request,"users/edit_profile_picture.html",
        {
            "form": form,
            "profile": profile
        }
    )


@login_required
def edit_contact_address(request):
    profile = request.user.profile  # OneToOneField ensures this exists
    form = EditContactAddressForm(request.POST, instance=profile)
    if request.method == 'POST':
        # form = EditContactAddressForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your contact and address information has been updated successfully!")
            return redirect('users:edit_contact_address')
        else:
            messages.error(request, "Please fix the errors below.")

        

    return render(request, 'users/edit_contact_address.html', {'form': form})

def edit_contact_address(request):
    return render(request,"users/contactus.html")