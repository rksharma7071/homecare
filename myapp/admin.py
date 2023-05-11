from django.contrib import admin
from .models import *


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('USER', 'FULL_NAME', 'EMAIL', 'PHONE_NUMBER','ADDRESS', 'CITY', 'STATE', 'TRADE','IMAGE')
# admin.site.register(Registration, RegistrationAdmin)



@admin.register(Contactus)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

