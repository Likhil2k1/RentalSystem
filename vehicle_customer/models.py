from django.core import validators
from django.db import models
from django.core.validators import *

# Create your models here.

class VehicleCustomer(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = ( ('Male','MALE') , ('Female','FEMALE')  )
    gender = models.CharField(max_length=100, blank=False, choices=gender_choices)
    username = models.CharField(max_length=100, blank=False, primary_key=True)
    mobileno = models.CharField(max_length=13, blank=False, validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=10)])
    city = models.CharField(max_length=100, blank=False)
    pincode = models.IntegerField(blank=False, validators=[MinValueValidator(limit_value=100000, message="Enter a 6-digit pincode"), MaxValueValidator(limit_value=999999, message="Enter a 6-digit pincode")])
    aadhar = models.BigIntegerField(blank=False, validators=[MinValueValidator(limit_value=100000000000, message="Enter a 12-digit number"), MaxValueValidator(limit_value=999999999999, message="Enter a 12-digit number")])
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(limit_value=6)])
    
    class Meta:
        db_table = "vehiclecustomer_table"


class Orders(models.Model):
    customer_name = models.CharField(max_length=100, blank=False)
    vehicle_type = models.CharField(max_length=100, blank=False)
    vehiclename = models.CharField(max_length=10, blank=False)
    capacity = models.PositiveIntegerField(blank=False)
    vehicleno = models.CharField(max_length=200,blank=False, validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=10)])
    description = models.CharField(max_length=250, blank=False)
    owner_name = models.CharField(max_length=100, blank=False)
    owner_mobile = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=10)])
    rentperday = models.DecimalField(decimal_places=2, max_digits=65, blank=False)
    days = models.DecimalField(decimal_places=2, max_digits=65, blank=False)
    totalrent = models.DecimalField(decimal_places=2, max_digits=65, blank=False)

    class Meta:
        db_table = "vehicles_orders"