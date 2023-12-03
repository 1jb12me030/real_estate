from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomAdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    type_choices = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    ]
    unit_type = models.CharField(max_length=4, choices=type_choices)

    def __str__(self):
        return f"{self.property.name} - {self.unit_type}"

class Tenant(models.Model):
    user = models.OneToOneField(CustomAdminUser, on_delete=models.CASCADE)
    address = models.TextField()
    document_proofs = models.TextField()

    def __str__(self):
        return self.user.email

class RentalInformation(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tenant.user.email} - {self.unit.property.name}"
