# Generated by Django 2.2.14 on 2021-05-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclecustomer',
            name='aadhar',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='vehiclecustomer',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
