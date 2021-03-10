from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', home, name='index'),
    path('about.html', about, name='about'),
    # path('services.html', services, name='services'),
    path('portfolio.html', portfolio, name='portfolio'),
    # path('price.html', price, name='price'),
    path('contact.html', contact, name='contact'),
]
