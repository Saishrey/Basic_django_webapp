from django.shortcuts import render, HttpResponse
from datetime import date
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    # return HttpResponse('this is homepage')
    context = {
        'var1': "I'm the best",
        'var2': "You're the best"
    }
    # messages.success(request, "This is test msg")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')
        contact = Contact(name=name, email=email, phone=phone, comments=comments, date=date.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')

    return render(request, 'contact.html')