from django.shortcuts import render
from django.http import HttpResponse
from portapp.models import *
from portapp.forms import *

# Create your views here.


def index(request):
    return render(request, 'portapp/index.html')


def download(request):
    return render(request, 'portapp/download.html')    