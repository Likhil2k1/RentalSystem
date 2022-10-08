from django.urls import path, include
from . import views

urlpatterns = [
    path('vehicles/vehicles_ownerlogin/', views.vehicles_ownerlogin, name='vehicles_ownerlogin'),
    path('vehicles/vehicles_ownerregister/', views.vehicles_ownerregister, name='vehicles_ownerregister'),
    path('vehicles/v_owner_home/', views.v_owner_home, name="v_owner_home"),
    path('vehicles/vehicles_ownerlogout/', views.vehicles_ownerlogout, name='vehicles_ownerlogout'),
    path('vehicles/v_owner_profile/', views.v_owner_profile, name='v_owner_profile'),
    path('vehicles/v_owner_requests/', views.v_owner_requests, name='v_owner_requests'),
    path('vehicles/v_owner_add/', views.v_owner_add, name='v_owner_add'),
    path('vehicles/v_owner_manage/', views.v_owner_manage, name='v_owner_manage'),
    path('vehicles/v_destroy/', views.v_destroy, name='v_destroy'),
    path('vehicles/v_update/', views.v_update, name='v_update'),

]
