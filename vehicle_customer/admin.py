from vehicle_customer.models import VehicleCustomer
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Orders)
admin.site.register(VehicleCustomer)
