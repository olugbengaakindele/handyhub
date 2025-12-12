from django.shortcuts import render, redirect
from django.http import HttpResponse as hp
from .forms import *
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def add_service_category(request):
    if request.method == "POST":
        form = ServiceCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect("users:index")
    else:
        form = ServiceCategoryForm()

    return render(request, "services/add_service_category.html", {"form": form})