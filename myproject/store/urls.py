from django.urls import path
from . views import index, about, resume, services, portfolio, contact, service_details
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('resume/', resume, name='resume'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    # <int:pk>/ this is use for primary key pass
    path('services/service_details/<int:pk>/', service_details, name='service_details'),
]
