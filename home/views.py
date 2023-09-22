from django.shortcuts import render
from .models import Staff, Services, Album, Blog, Message_to_Admin
# Create your views here.

def index(request):
    import time

    if request.POST:
        name = request.POST.get('text')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        company_name = request.POST.get('company-name')
        message = request.POST.get('message')

        Message_to_Admin.objects.create(full_name=name, email=email, subject=subject, company_name=company_name, message=message)



    data = {
        'devs': Staff.objects.all(),
        'services': Services.objects.all(),
        'albums': Album.objects.all(),
        'blogs': Blog.objects.all(),
        'day': time.strftime("%d"),
        'month': time.strftime("%b")
    }

    return render(request, 'index.html', data)