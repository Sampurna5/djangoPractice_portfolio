from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


    # def services(request):
    #     return render(request, 'services.html')


def portfolio(request):
    return render(request, 'portfolio.html')


# def price(request):
#     return render(request, 'price.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        data.save()
        success_message = {'message': 'Your query was received!!'}
        return render(request, 'contact.html', success_message)

    return render(request, 'contact.html')
