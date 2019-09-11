from django.http import HttpResponse
from django.shortcuts import render
from blog.models import *


# Create your views here.
def index(request):
    lst_sub = Subject.objects.all()
    return render(request, 'pages/home.html', {'lst_sub': lst_sub})


def error(request):
    return render(request, 'pages/404.html')


def About(request):
    return render(request, 'pages/about.html')


def Contact(request):
    return render(request, 'pages/contact.html')


def ADV(request):
    return render(request, 'pages/adv.html')


def ADVContact(request):
    return render(request, 'pages/advcontact.html')
