from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('home from Python!')
    return render(request, 'index.html')

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def services(request):
    return render(request, 'services.html')

def consultation(request):
    return render(request, 'consultation.html')
