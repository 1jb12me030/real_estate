from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def admin_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Use 'username' to get email
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin_home')  # Redirect to your admin home page
    else:
        form = AuthenticationForm()
    return render(request, 'testapp/admin_login.html', {'form': form})

# views.py
from django.shortcuts import render

def admin_home(request):
    return render(request, 'testapp/admin_home.html')  



# views.py
from django.shortcuts import render
from .models import Property, Unit, Tenant, RentalInformation

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'testapp/property_list.html', {'properties': properties})

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'testapp/tenant_list.html', {'tenants': tenants})



# views.py
from django.shortcuts import render, get_object_or_404
from .models import Property, Unit, Tenant

def property_profile(request, property_id):
    property_instance = get_object_or_404(Property, pk=property_id)
    units = Unit.objects.filter(property=property_instance)
    unit_tenant_info = []
    for unit in units:
        try:
            tenant_info = Tenant.objects.get(rentalinformation__unit=unit)
            unit_tenant_info.append({'unit': unit, 'tenant': tenant_info})
        except Tenant.DoesNotExist:
            unit_tenant_info.append({'unit': unit, 'tenant': None})
    return render(request, 'testapp/property_profile.html', {'property': property_instance, 'unit_tenant_info': unit_tenant_info})


# views.py
from django.shortcuts import render, get_object_or_404
from .models import Tenant, RentalInformation
def tenant_profile(request, tenant_id):
    tenant_instance = get_object_or_404(Tenant, pk=tenant_id)
    rental_info = RentalInformation.objects.filter(tenant=tenant_instance).first()
    return render(request, 'testapp/tenant_profile.html', {'tenant': tenant_instance, 'rental_info': rental_info})

