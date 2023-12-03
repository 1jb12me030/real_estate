from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CustomAdminUser)
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(RentalInformation)