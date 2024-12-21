from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  profile_id = models.BigAutoField(primary_key=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_image = models.ImageField(upload_to='profile_image', default='static/default_images/blank-profile-picture.webp')
  phone_number = models.CharField(max_length=15)
  Bio = models.TextField()
  
  def __str__(self):
    return self.user.first_name



class Listing(models.Model):
  listing_id = models.BigAutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  property_status = models.CharField(max_length=10)
  property_type = models.CharField(max_length=10)
  lux_type = models.CharField(max_length=20)
  title = models.CharField(max_length=255)
  area = models.PositiveIntegerField()
  price = models.IntegerField()
  beds = models.PositiveIntegerField()
  baths = models.PositiveIntegerField()
  floor = models.CharField(max_length=12)
  elevator = models.CharField(max_length=5)
  parking = models.CharField(max_length=5)
  location = models.CharField(max_length=20)
  description = models.TextField(help_text='')
  slug = models.SlugField()

  def __str__(self):
    return self.title


class Upload(models.Model):
  listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
  images = models.ImageField(upload_to='listing_images')

  def __str__(self):
    return self.listing.title
  
  