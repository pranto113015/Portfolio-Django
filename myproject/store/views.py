from django.shortcuts import render

# This is manual import file for take input backend
from .models import About 
from .models import Feature
from .models import Testimonial


# Create your views here.


def index(request):
    return render(request, 'index.html')



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


def services(request):
    return render(request, 'services.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    return render(request, 'contact.html')
