from django.contrib import admin
from .models import *


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('FULL_NAME', 'EMAIL', 'PHONE_NUMBER', 'CITY', 'STATE', 'TRADE','IMAGE')
# admin.site.register(Registration, RegistrationAdmin)



@admin.register(Contactus)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

