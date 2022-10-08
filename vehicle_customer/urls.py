from django.urls import path, include
from . import views

urlpatterns = [
    path('vehicles/vehicles_customerlogin/', views.vehicles_customerlogin, name='vehicles_customerlogin'),
    path('vehicles/vehicles_customerlogout/', views.vehicles_customerlogout, name='vehicles_customerlogout'),
    path('vehicles/vehicles_customerregister/', views.vehicles_customerregister, name='vehicles_customerregister'),
    path('vehicles/v_customer_home/', views.v_customer_home, name="v_customer_home"),
    path('vehicles/v_customer_profile/', views.v_customer_profile, name='v_customer_profile'),
    path('vehicles/v_customer_search/', views.v_customer_search, name='v_customer_search'),
    path('vehicles/v_customer_searchresults/', views.v_customer_searchresults, name='v_customer_searchresults'),
    
    path('vehicles/v_customer_rentvehicle/', views.v_customer_rentvehicle, name = 'v_customer_rentvehicle'),
    path('vehicles/v_customer_request/', views.v_customer_request, name = 'v_customer_request'),
    path('vehicles/v_confirm/', views.v_confirm, name = 'v_confirm'),
    path('vehicles/vehicles_customerbookings/', views.vehicles_customerbookings, name = 'vehicles_customerbookings'),
    
]