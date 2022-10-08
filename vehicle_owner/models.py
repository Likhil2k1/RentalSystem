from django.core import validators
from django.db import models
from django.core.validators import *
from django.db.models.aggregates import Max

# Create your models here.

class VehicleOwner(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = ( ('Male','MALE') , ('Female','FEMALE')  )
    gender = models.CharField(max_length=100, blank=False, choices=gender_choices)
    username = models.CharField(max_length=100, blank=False, primary_key=True)
    mobileno = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=10)])
    city = models.CharField(max_length=100, blank=False)
    pincode = models.IntegerField(blank=False, validators=[MinValueValidator(limit_value=100000, message="Enter a 6-digit pincode"), MaxValueValidator(limit_value=999999, message="Enter a 6-digit pincode")])
    aadhar = models.BigIntegerField(blank=False, validators=[MinValueValidator(limit_value=100000000000, message="Enter a 12-digit number"), MaxValueValidator(limit_value=999999999999, message="Enter a 12-digit number")])
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(limit_value=6)])
    
    class Meta:
        db_table = "vehicleowner_table"


class Vehicles(models.Model):
    owner_name = models.CharField(max_length=100,blank=False)
    type_choices = (('default','Select Type'),('Bike','BIKE'), ('Car','CAR'))
    type = models.CharField(max_length=100,blank=False,choices=type_choices,default='default')
    vehiclename = models.CharField(max_length=100, blank=False)
    capacity = models.PositiveIntegerField(blank=False)
    vehicleno = models.CharField(max_length=200,blank=False,primary_key=True, validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=10)])
    image1 = models.ImageField(upload_to='static/images/vehicles/')
    image2 = models.ImageField(upload_to='static/images/vehicles/')
    image3 = models.ImageField(upload_to='static/images/vehicles/')
    description = models.CharField(max_length=250,blank=False)
    rent = models.DecimalField(decimal_places=2, max_digits=65)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        db_table = "owner_vehicles"