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
    age = models.IntegerField(max_length=10)
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    bottom_short_discription = models.CharField(max_length=200)



class Feature(models.Model):
    icon = models.CharField(max_length=100)
    interested_title = models.CharField(max_length=50)


class Testimonial(models.Model):
    t_discription = models.CharField(max_length=250)
    name = models.CharField(max_length=80)
    t_designation = models.CharField(max_length=100)
    


class Social(models.Model):
   social_icon=models.CharField(max_length=100)
   link=models.URLField(max_length=1000)


   def __str__(self):
    return self.social_icon


