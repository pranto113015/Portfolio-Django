from django.shortcuts import render

# This is manual import file for take input backend
from .models import About  
from .models import Social  
from .models import Feature
from .models import Testimonial
from .models import Service


# Create your views here.

# index/home section function
def index(request):
    social= Social.objects.all()
    return render(request, 'index.html',{'social':social})



# about section function
def about(request):
    # data pick one time one by one so use get() method
    about = About.objects.get()
    # data pick all object use all() method
    feature = Feature.objects.all() #interseted section function
    testimonial = Testimonial.objects.all() # testimonial section function
    return render(request, 'about.html',{'about':about, 'feature':feature, 'testimonial':testimonial})
    


def resume(request):
    return render(request, 'resume.html')

# service section function
def services(request):
    services=Service.objects.all()
    return render(request, 'services.html',{'services':services})

def service_details(request):
    return render(request, 'service_details.html')



def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    return render(request, 'contact.html')
