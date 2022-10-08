from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import VehicleCustomer, Orders
from .forms import VehicleCustomerForm, SearchForm
from django.db.models import Q
from vehicle_owner.models import Vehicles, VehicleOwner
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def vehicles_customerregister(request):
    if request.method == 'POST':
        form = VehicleCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'vehicles_customerlogin.html')
    else:
        form = VehicleCustomerForm()
    return render(request,'vehicles_customerregister.html',{'form':form})


def vehicles_customerlogin(request):
    if request.method == 'POST':
        username = request.POST["name"]
        password = request.POST["pwd"]
        flag = VehicleCustomer.objects.filter(Q(username__iexact=username) & Q(password__iexact=password))
        if flag:
            request.session['username'] = username
            return redirect('v_customer_home')
        else:
            return render(request,'vehicles_customerloginfailed.html', {'message': 'Wrong Username / Password.'})
    else:
        return render(request,'vehicles_customerlogin.html')


def vehicles_customerlogout(request):
    request.session['username'] = ""
    return render(request, 'vehicles_customerlogin.html')


def v_customer_home(request):
    username = request.session["username"]    
    all_vehicles = Vehicles.objects.all()
    return render(request, 'v_customer_home.html', {'username': username, 'all_vehicles': all_vehicles})


def v_customer_profile(request): 
    uname = request.session["username"]
    obj = VehicleCustomer.objects.get(username=uname)
    context = {
        'object': obj,
        'username': uname,
    }
    return render(request, "v_customer_profile.html", context)
    
  
def v_customer_search(request):
    username = request.session["username"]
    return render(request, 'v_search.html', {'username':username})
    

def v_customer_searchresults(request):
    username = request.session["username"]
    if request.method == "POST":
        type = request.POST["type"]
        vehiclename = request.POST["vehiclename"]
        capacity = request.POST["capacity"]
        vehicles = Vehicles.objects.filter(vehiclename=vehiclename,type=type,capacity=capacity)
        count = Vehicles.objects.filter(vehiclename=vehiclename,type=type,capacity=capacity).count()
        return render(request, 'v_search_results.html', {'vehicles': vehicles, 'count': count, 'username': username})
    else:
        return render(request, 'v_search.html', {'username': username})
     












def v_customer_rentvehicle(request):
    username = request.session["username"]
    if request.method == 'POST':
        vehicleno = request.POST['vehicleno']
        owner_name = request.POST['owner_name']
        vehicles = Vehicles.objects.filter(vehicleno=vehicleno,owner_name=owner_name)
        owner = VehicleOwner.objects.filter(fullname=owner_name)
        count = Vehicles.objects.filter(vehicleno=vehicleno,owner_name=owner_name).count()
        mylist = zip(vehicles, owner)
        return render(request, 'v_rent_proceed.html', {'mylist': mylist , 'count': count, 'username': username})
    else:
        return render(request, 'v_customer_home.html')


def v_customer_request(request):
    #return HttpResponse(request.POST['doorno'] + " " + request.POST['owner_name'] + " " + request.POST['customer_name'] + " " + request.POST['months'])
    username = request.session["username"]
    if request.method == 'POST':
        doorno = request.POST['doorno']
        owner_name = request.POST['owner_name']
        vehicle = Vehicles.objects.filter(doorno=doorno,owner_name=owner_name)
        owner = VehicleOwner.objects.filter(fullname=owner_name)
        mylist = zip(vehicle, owner)
        return render(request, 'confirmation.html', {'mylist':mylist})
        

def v_confirm(request):
    #return HttpResponse('HELLO')
    username = request.session["username"]
    if request.method == 'POST':
        vehicleno = request.POST['vehicleno']
        owner_name = request.POST['owner_name']
        rentperday = float(request.POST['rentperday'])
        days = float(request.POST['days'])
        totalrent = rentperday * days
        vehicles = Vehicles.objects.filter(vehicleno=vehicleno,owner_name=owner_name)
        owners = VehicleOwner.objects.filter(fullname=owner_name)
        customers = VehicleCustomer.objects.filter(fullname = username)
        mylist = zip(vehicles, owners, customers)
        
        for vehicle, owner, customer in mylist:
            if vehicle.is_available == True:
                try:
                    order = Orders()
                    order.customer_name = username
                    order.vehicle_type = vehicle.type
                    order.vehiclename = vehicle.vehiclename                    
                    order.capacity = vehicle.capacity
                    order.vehicleno = vehicleno
                    order.description = vehicle.description
                    order.owner_name = vehicle.owner_name
                    order.owner_mobile = owner.mobileno
                    order.rentperday = rentperday
                    order.days = days
                    order.totalrent = totalrent
                    order.save()

                    v_owner_email = owner.email
                    v_customer_email = customer.email

                except:
                    order = Orders.objects.get(customer_name = username, vehicle_type = vehicle.type,  vehiclename = vehicle.vehiclename, capacity = vehicle.capacity, vehicleno = vehicleno, description = vehicle.description, owner_name = vehicle.owner_name, owner_mobile = owner.mobileno, rentperday = rentperday, days = days, totalrent = totalrent)
                vehicle.is_available = False
                vehicle.save()

                #SENDING CONFIRMATION MAIL
                c_message = "ORDER PLACED !!!\nHello {},\n\nYour order is confirmed !!! Thank you for choosing us and being a part of our journey.\n\n\nOrder Details are:\n------------------\nVehicle type:\t{}\nVehicle Name:\t{}\nCapacity:\t{}\nVehicle Number:\t{}\nOwner Name:\t{}\nOwner Mobile:\t{}\nOwner Email:\t{}\nRent(Rs.)/day:\t{}\nDays:\t{}\nTotal Rent:\t{}".format(username, order.vehicle_type, order.vehiclename, order.capacity, order.vehicleno, order.owner_name, order.owner_mobile, v_owner_email, order.rentperday, order.days, order.totalrent)
                o_message = "NEW CUSTOMER ORDER !!!\nYou received an order from {}.\n\n\nOrder Details are:\n------------------\nCustomer Name:\t{}\nCustomer Mobile:\t{}\nCustomer Email:\t{}\nVehicle Type:\t{}\nVehicle Name:\t{}\nCapacity:\t{}\nVehicle Number:\t{}\nRent(Rs.)/day:\t{}\nDays:\t{}\nTotal Rent:\t{}".format(username, customer.fullname, customer.mobileno, v_customer_email, order.vehicle_type, order.vehiclename, order.capacity, order.vehicleno, order.rentperday, order.days, order.totalrent)
                send_mail("Order Confirmation", c_message, settings.EMAIL_HOST_USER, [v_customer_email]) # To Customer
                send_mail("Order Confirmation", o_message, settings.EMAIL_HOST_USER, [v_owner_email]) # To Owner

                return render(request, 'v_confirm.html', {'mylist':mylist, 'order': order, 'username': username})
        else:
            return render(request, 'v_order_failed.html')


def vehicles_customerbookings(request):
    username = request.session["username"]
    count = Orders.objects.filter(customer_name=username).count()
    orders = Orders.objects.filter(customer_name=username)
    return render(request, 'v_customer_bookings.html', {'username': username, 'orders':orders, 'count': count})


