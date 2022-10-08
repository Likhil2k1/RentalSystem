# Generated by Django 2.2.14 on 2021-05-18 09:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_owner', '0011_auto_20210518_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleowner',
            name='aadhar',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(limit_value=100000000000, message='Enter a 12-digit number'), django.core.validators.MaxValueValidator(limit_value=999999999999, message='Enter a 12-digit number')]),
        ),
    ]
