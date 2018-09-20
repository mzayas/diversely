from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User
from .forms import RegisterForm
# Create your views here.

def RegisterView(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = RegisterForm()

        args = {'form': form}
        return render(request, 'register.html', args)

def login(request):
    # return HttpResponse('home from Python!')
    return render(request, 'login.html')    
