from django.shortcuts import render
from django.http import HttpResponse as hp


def index(request):
    return render(request, "users/base.html")

def register(request):

    return render(request, "users/register.html")