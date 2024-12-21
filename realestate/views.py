from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Profile, Listing, Upload
import os

# Create your views here.


def register(request):

  if request.method == 'POST':
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
    password1 = request.POST.get('pass1')
    password2 = request.POST.get('pass2')
    passcode1 = request.POST.get('passcode')
    passcode2 = '00000'

    if password1 == password2:
      if passcode1 == passcode2:
        if User.objects.filter(email=email).exists():
          messages.info(request, 'An account with Email Already exist')
          return redirect('register')
        else:
          user = User.objects.create_user(username=email, last_name=last_name,
          email=email,password=password1,first_name=first_name)
          user.save()
          return redirect('homepage')
      else:
        messages.info(request, 'Passcode Incorrect!')
        return redirect('register')
    else:
      messages.info(request, 'Password Does Not Match!')
      return redirect('register')

  return render(request, 'realestate/register.html')



def login(request):
  
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = auth.authenticate(username=email, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('homepage')
    else:
      messages.info(request, 'User is not found!')
      return redirect('login')

  return render(request, 'realestate/login.html')


def logout(request):
  auth.logout(request)
  return redirect('homepage')
  

def homepage(request):
  listings = Listing.objects.all()
  
  context = {
    'listings': listings
  }
  return render(request, 'realestate/homepage.html', context)


def create_property(request):

  if request.method == 'POST':
    property_status = request.POST.get('property_status')
    property_type = request.POST.get('property_type')
    lux_type = request.POST.get('lux_type')
    title = request.POST.get('title')
    images = request.FILES.getlist('images')
    area = request.POST.get('area')
    price = request.POST.get('price')
    baths = request.POST.get('number_of_baths')
    beds = request.POST.get('number_of_beds')
    floor = request.POST.get('floor')
    elevator = request.POST.get('elevator')
    parking = request.POST.get('parking')
    description = request.POST.get('description')
    location = request.POST.get('location')

    for i in images:
      uploads = Upload.objects.create(images=i)

    listing = Listing.objects.create(listing_id=uploads.id,user=request.user,property_status=property_status,
      property_type=property_type,lux_type=lux_type,title=title,upload=uploads,
      area=area,price=price,baths=baths,beds=beds,location=location,floor=floor,
      elevator=elevator,parking=parking,description=description)
    return redirect('homepage')

    #listing = Listing.objects.create(user=request.user,property_status=property_status,
    #property_type=property_type,lux_type=lux_type,title=title,images=images,
    #area=area,price=price,baths=baths,beds=beds,location_name=location1,floor=floor,
    #elevator=elevator,parking=parking,description=description)

    #listing.save()
    #return redirect('homepage')


  return render(request, 'realestate/create_property.html')


def property_details(request,pk):
  listing = get_object_or_404(Listing,listing_id=pk)
  context = {
    'listing': listing
  }
  return render(request, 'realestate/property_details.html', context)



def update_property(request, pk):
  listing = get_object_or_404(Listing,listing_id=pk)

  if request.method == 'POST':
    if request.FILES:
      if len(listing.images) > 0:
        os.remove(listing.images.path)
      listing.images = request.FILES.get('images')
    listing.property_status = request.POST.get('property_status')
    listing.property_type = request.POST.get('property_type')
    listing.lux_type = request.POST.get('lux_type')
    listing.title = request.POST.get('title')
    listing.area = request.POST.get('area')
    listing.price = request.POST.get('price')
    listing.baths = request.POST.get('number_of_baths')
    listing.beds = request.POST.get('number_of_beds')
    listing.floor = request.POST.get('floor')
    listing.elevator = request.POST.get('elevator')
    listing.parking = request.POST.get('parking')
    listing.description = request.POST.get('description')
    listing.location = request.POST.get('location')

    listing.save()
    return redirect('homepage')


  context = {
    'listing': listing
  }
  return render(request, 'realestate/edit_property.html', context)

def delete_property(request,pk):
  listing = get_object_or_404(Listing, listing_id=pk)
  listing.delete()
  return redirect('homepage')


def search(request):
  return render(request, 'realestate/search.html')


def agents(request):
  return render(request, 'realestate/agents.html')

def agent_details(request):
  pass