from django.shortcuts import render
from django.urls import path
from . import views
from .models import *
urlpatterns = [
    path('',views.index),
    path('about-us',views.About),
    path('contact',views.Contact),
    path('advertise',views.ADV),
    path('advertising',views.ADVContact),
]
