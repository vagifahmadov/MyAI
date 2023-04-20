from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Services)
admin.site.register(Pages)


class AdminVR(admin.ModelAdmin):
    list_display = ("title",)

