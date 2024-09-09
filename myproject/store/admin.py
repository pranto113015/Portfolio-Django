from django.contrib import admin
from .models import About
from .models import Feature
from .models import Testimonial
from .models import Social

# Register your models here.
admin.site.register(About)
admin.site.register(Feature)
admin.site.register(Testimonial)
admin.site.register(Social)