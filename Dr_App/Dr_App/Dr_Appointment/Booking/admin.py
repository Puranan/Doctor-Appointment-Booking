from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(contact)

class name(admin.ModelAdmin):
    list_display = ("NAME1",)
admin.site.register(Senthil_Booking,name)


class name(admin.ModelAdmin):
    list_display = ("NAME1",)
admin.site.register(afsalas_Booking,name)


class name(admin.ModelAdmin):
    list_display = ("name","age")
admin.site.register(texasapp,name)

class name(admin.ModelAdmin):
    list_display = ("NAME1",)

admin.site.register(Andrew_Booking,name)

class name(admin.ModelAdmin):
    list_display = ("NAME1",)

admin.site.register(vikram_Booking,name)