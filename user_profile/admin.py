from django.contrib import admin

from .models import Profile, Tags, Site

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(Site)