from django.shortcuts import render

# Create your views here.
def diagnostics(request):
    # return HttpResponse('home from Python!')
    return render(request, 'diagnostics.html')
