from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.http import HttpResponse
from myapp.models import *


def home(request):
    return render(request, 'home.html', locals())


def catalog(request):
    return render(request, 'catalog.html')


def offer(request):
    return render(request, 'offers.html')


def services(request):
    return render(request, 'services.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            error = 'no'
            Contactus.objects.create(name=name, email=email, subject=subject, message=message)
        except Exception:
            error='yes'
    return render(request, 'contactus.html', locals())


def emp_record(request):
    registrations = Registration.objects.all()
    return render(request, 'emp_record.html', locals())


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Thank you for registering!')
            # return render(request, 'emp_record.html', locals())
            return redirect('emp_record')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
