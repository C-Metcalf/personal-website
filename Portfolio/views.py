from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.


def portfolio(request):
    if request.method == 'POST':
        pass

    return render(request, 'Portfolio/index.html')


def projects(request):
    return render(request, 'Portfolio/projects.html')


def resume(request):
    return render(request, 'Portfolio/resume.html')


def contact(request):
    return render(request, 'Portfolio/contact.html')


