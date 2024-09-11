from django.db import models

# Create your models here.

class About(models.Model):
    about_discription = models.CharField(max_length=250)
    designation = models.CharField(max_length=100)
    designation_short_discription = models.CharField(max_length=200)
    birth_date = models.DateField()
    website_link = models.URLField(max_length=300)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    bottom_short_discription = models.CharField(max_length=200)

    def __str__(self):
     return self.designation





class Feature(models.Model):
    icon = models.CharField(max_length=100)
    icon_color=models.CharField(max_length=100,default='#fff')
    interested_title = models.CharField(max_length=50)


    def __str__(self):
     return self.interested_title





class Testimonial(models.Model):
    t_discription = models.CharField(max_length=250)
    name = models.CharField(max_length=80)
    t_designation = models.CharField(max_length=100)
    image= models.ImageField(upload_to='testimonials_img/', default='#')
    
    def __str__(self):
     return self.name





class Social(models.Model):
   social_icon=models.CharField(max_length=100)
   link=models.URLField(max_length=1000)


   def __str__(self):
    return self.social_icon





class Service(models.Model):
    s_icon=models.CharField(max_length=100)
    s_title=models.CharField(max_length=100)
    s_image=models.ImageField(upload_to='service_img/', blank=True, null=True)
    s_description=models.CharField(max_length=500)

    def __str__(self):
      return self.s_title
     

