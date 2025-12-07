from django.shortcuts import render
from django.http import HttpResponse as hp


def index(request):

    return hp("This is my first app")
