
from django.urls import path
from .views import *



urlpatterns = [
    path('login/', admin_login_view, name='admin_login'),
    path('admin_home/', admin_home, name='admin_home'),
    path('properties/', property_list, name='property_list'),
    path('tenants/', tenant_list, name='tenant_list'),
    path('property/<int:property_id>/', property_profile, name='property_profile'),
    path('tenant/<int:tenant_id>/', tenant_profile, name='tenant_profile'),
    
    
]
