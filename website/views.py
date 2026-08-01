from django.shortcuts import render

from django.urls import path
from . import views


def home(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def blog(request):
    return render(request, 'website/blog.html')


def contact(request):
    return render(request, 'website/contact.html')


def service(request):
    return render(request, 'website/service.html')


def testimonial(request):
    return render(request, 'website/testimonail.html')