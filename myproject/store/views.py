from django.shortcuts import render,redirect

# This is manual import file for take input backend
from .models import *
from .forms import ContactForm


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


# image passing from service to service details usign pk=primary key
def service_details(request,pk): 
    service_details=Service.objects.get(pk=pk)
    return render(request, 'service_details.html',{'service_details':service_details})



def portfolio(request):
    return render(request, 'portfolio.html')




def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    return render(request, "contact.html", {'form':form})
