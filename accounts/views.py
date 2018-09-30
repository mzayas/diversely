from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User
from .forms import RegisterForm
# Create your views here.

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
