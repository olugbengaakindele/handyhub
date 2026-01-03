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
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .utils import get_service_area_limit
from django.db import transaction



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

    if request.method == "POST":
        if form.is_valid():
            user = form.save()

            # Optional: log user in immediately
            login(request, user)

            # Optional: redirect based on account type
            account_type = user.profile.account_type
            if account_type == "tradesperson":
                return redirect("users:profile")  # private dashboard
            else:
                return redirect("users:index")  # or "find service" page

        messages.error(request, "Please fix the errors below.")

    return render(request, "users/register.html", {"form": form})



@login_required
def profile(request):
    user = request.user
    profile = getattr(user, "profile", None)
    user_services = (
        UserService.objects
        .select_related("category", "subcategory")
        .filter(user=user)
    )

    user_service_areas = ServiceArea.objects.filter(userservicearea__user=user)

    context = {
        "user_obj": user,
        "profile": profile,
        "user_services": user_services,
        "user_has_services": user_services.exists(),
        "user_service_areas": user_service_areas,
    }
    return render(request, "users/profile.html", context)


@login_required
def logmeout(request):
    logout(request)
    messages.success(request,f"You have been logout of of this app")
    return redirect("users:index")


# this adds services to a user
@login_required
def add_user_services(request):
    # 🔐 Security: users can only edit their own services
    # if request.user.id != userid:
    #     return redirect("users:profile", request.user.id)
    user = request.user

    user_services = (
        UserService.objects
        .select_related("category", "subcategory")
        .filter(user=user)
    )

    categories = ServiceCategory.objects.prefetch_related("subcategories")

    if request.method == "POST":
        category_id = request.POST.get("category")
        selected_services = request.POST.getlist("services")

        if not category_id or not selected_services:
            messages.error(request, "Please select a category and at least one service.")
            return redirect("users:profile", user.id)

        category = get_object_or_404(ServiceCategory, id=category_id)

        existing_count = user.services.count()
        remaining_slots = 5 - existing_count

        if remaining_slots <= 0:
            messages.error(
                request,
                "You have already added the maximum of 5 services."
            )
            return redirect("users:profile", user.id)

        # Only allow adding up to remaining slots
        services_to_add = selected_services[:remaining_slots]

        for sub_id in services_to_add:
            UserService.objects.get_or_create(
                user=user,
                category=category,
                subcategory_id=sub_id
            )

        if len(selected_services) > remaining_slots:
            messages.warning(
                request,
                f"Only {remaining_slots} service(s) were added. "
                "Free accounts can have a maximum of 5 services."
            )

        return redirect("users:profile", user.id)

    context = {
        "user_obj": user,
        "user_services": user_services,
        "categories": categories,
        "max_services": 5,
        "current_count": user.services.count(),
    }

    return render(request, "users/userservices.html", context)

@login_required
def edit_profile(request):
    profile = request.user.profile  # guaranteed by signal

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("users:profile")
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
        return redirect("users:userservice")

    if request.method == "POST":
        service.delete()
        messages.success(request, "Service removed successfully.")
        return redirect("users:userservice")

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
            return redirect("users:profile" )
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

# this edits the contact information
@login_required
def edit_contact_info(request):
    profile = request.user.profile  # existing DB record

    if request.method == "POST":
        form = EditContactForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact information updated successfully.")
            return redirect("users:profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        # ✅ THIS is what prefills the form
        form = EditContactForm(instance=profile)

    return render(
        request,
        "users/edit_contact_info.html",
        {"form": form},
    )
        

    return render(request, 'users/edit_contact_info.html', {'form': form})

@login_required
def edit_address_info(request):
    profile = request.user.profile  # OneToOneField ensures this exists
    
    if request.method == 'POST':
        form = EditAddressForm(request.POST, instance=profile)
        # form = EditContactAddressForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your address information has been updated successfully!")
            return redirect('users:profile')
        else:
            messages.error(request, "Please fix the errors below.")
    else :
        form = EditAddressForm( instance=profile)  

    return render(request, 'users/edit_address_info.html', {'form': form})



def contactus(request):
    return render(request,"users/contactus.html")



@login_required
def edit_service_areas(request):
    user = request.user
    service_area_limit = get_service_area_limit(user)

    # All possible areas (for checkbox selection)
    all_areas = ServiceArea.objects.filter(is_active=True).order_by("metro_city", "city", "name")

    # User's currently selected areas (via reverse relation name in error choices: userservicearea)
    selected_area_objects = ServiceArea.objects.filter(userservicearea__user=user).order_by("metro_city", "city", "name")
    selected_ids_current = set(selected_area_objects.values_list("id", flat=True))

    if request.method == "POST":
        selected_ids_post = request.POST.getlist("service_areas")
        selected_ids_post = [int(x) for x in selected_ids_post if x.isdigit()]

        # ✅ Enforce free tier max
        if len(selected_ids_post) > service_area_limit:
            messages.error(
                request,
                f"Free tier users can only select up to {service_area_limit} service areas."
            )
            # Re-render page with current context (don’t save)
            return render(
                request,
                "users/edit_service_areas.html",
                {
                    "all_areas": all_areas,
                    "selected_areas": selected_ids_post,  # show what they tried
                    "selected_area_objects": selected_area_objects,
                    "service_area_limit": service_area_limit,
                },
            )

        # Save selections: wipe and recreate links
        with transaction.atomic():
            UserServiceArea.objects.filter(user=user).delete()

            links = [
                UserServiceArea(user=user, service_area_id=area_id, is_active=True)
                for area_id in selected_ids_post
            ]
            UserServiceArea.objects.bulk_create(links)

        messages.success(request, "Your service areas have been updated.")
        return redirect("users:edit_service_areas")

    # GET context
    context = {
        "all_areas": all_areas,
        "selected_areas": list(selected_ids_current),        # for checkbox checked state
        "selected_area_objects": selected_area_objects,      # for list below
        "service_area_limit": service_area_limit,
    }
    return render(request, "users/edit_service_areas.html", context)


@login_required
def delete_service_area_confirm(request, area_id):
    """
    Confirm + remove a service area from THIS user only.
    """
    link = get_object_or_404(UserServiceArea, user=request.user, service_area_id=area_id)

    if request.method == "POST":
        link.delete()
        messages.success(request, "Service area removed.")
        return redirect("users:edit_service_areas")

    return render(request, "users/confirm_delete_service_area.html", {"area": link})
