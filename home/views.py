from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('this is homepage')
    context = {
        'var1': "I'm the best",
        'var2': "You're the best"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')