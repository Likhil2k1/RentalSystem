from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehicles, VehicleOwner
from vehicle_customer.models import Orders
from .forms import VehicleOwnerForm, VehiclesForm
from django.db.models import Q


def vehicles_ownerregister(request):
    if request.method == 'POST':
        form = VehicleOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'vehicles_ownerlogin.html')
    else:
        form = VehicleOwnerForm()
    return render(request, 'vehicles_ownerregister.html', {'form': form})


def vehicles_ownerlogin(request):
    if request.method == 'POST':
        username = request.POST["name"]
        password = request.POST["pwd"]
        flag = VehicleOwner.objects.filter(Q(username__iexact=username) & Q(password__iexact=password))
        if flag:
            request.session['username'] = username
            return redirect('v_owner_home')
        else:
            return render(request,'vehicles_ownerloginfailed.html', {'message': 'Wrong Username / Password.'})
    else:
        return render(request, 'vehicles_ownerlogin.html')


def vehicles_ownerlogout(request):
    request.session['username'] = ""
    return render(request, 'vehicles_ownerlogin.html')


def v_owner_home(request):
    username = request.session["username"]
    return render(request, 'v_owner_home.html', {'username': username})

    
def v_owner_profile(request): 
    uname = request.session["username"]
    obj = VehicleOwner.objects.get(username=uname)
    context = {
        'object': obj,
        'username': uname,
    }
    return render(request, "v_owner_profile.html", context)


def v_owner_requests(request): 
    uname = request.session["username"]
    count = Orders.objects.filter(owner_name=uname).count()
    orders = Orders.objects.filter(owner_name=uname)
    context = {
        'orders': orders,
        'username': uname,
        'count': count,
    }
    return render(request, "v_owner_requests.html", context)


def v_owner_add(request): 
    username = request.session["username"]
    if request.method == 'POST':
        form = VehiclesForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.owner_name = username
            form1.save()
            return redirect('v_owner_profile')
    else:
        form = VehiclesForm()
    return render(request, 'v_owner_add.html', {'form': form, 'username': username})


def v_owner_manage(request): 
    username = request.session["username"]
    vehicles = Vehicles.objects.filter(owner_name=username)  
    count = Vehicles.objects.filter(owner_name=username).count()  
    return render(request, 'v_owner_manage.html', {'vehicles': vehicles, 'count': count, 'username': username})

def v_destroy(request):
    username = request.session["username"]
    if request.method == 'POST':
        vehicleno = request.POST['vehicleno']
        vehicle = Vehicles.objects.get(vehicleno=vehicleno)
        vehicle.delete()
        return redirect('v_owner_manage')

def v_update(request):
    username = request.session["username"]
    if request.method == 'POST':
        vehicleno = request.POST['vehicleno']
        vehicle = Vehicles.objects.get(vehicleno=vehicleno)
        form = VehiclesForm(request.POST, instance=vehicle)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.owner_name = username
            form1.save()
            return redirect('v_owner_manage')
        else:
            form = VehiclesForm()
    return render(request, 'v_owner_update.html', {'form': form, 'username': username, 'vehicle': vehicle})

 