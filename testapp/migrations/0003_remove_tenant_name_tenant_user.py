# Generated by Django 4.2.7 on 2023-12-02 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_property_tenant_unit_rentalinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='name',
        ),
        migrations.AddField(
            model_name='tenant',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
