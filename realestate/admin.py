from django.contrib import admin
from . models import Profile, Listing, Upload

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ['title']}

class UploadAdmin(admin.ModelAdmin):
  list_display = ['images',]

admin.site.register(Listing, ListingAdmin)
admin.site.register(Profile)
admin.site.register(Upload, UploadAdmin)