from django.shortcuts import render

# Create your views here.
def tools(request):
    # return HttpResponse('home from Python!')
    return render(request, 'tools.html')
