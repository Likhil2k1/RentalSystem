from django import forms
from .models import VehicleOwner, Vehicles


class VehicleOwnerForm(forms.ModelForm):
    class Meta:
        model = VehicleOwner
        fields = "__all__"
        labels = {
            'fullname': "",
            'gender': "Select Gender",
            'username': "",
            'mobileno': "",
            'city': "",
            'pincode': "",
            'aadhar': "",            
            'email': "",
            'password': "",
        }
        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'Enter FullName'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter UserName'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),
            'mobileno': forms.TextInput(attrs={'placeholder': 'Enter Mobile Number'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter City'}),
            'aadhar': forms.NumberInput(attrs={'placeholder': '     Enter Aadhar No.'}),
            'pincode': forms.NumberInput(attrs={'placeholder': '     Enter PINCODE'})
        }


class VehiclesForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        exclude = ('owner_name', 'is_available')
        labels = {
            'type': "",
            'vehiclename': "",
            'capacity': "",
            'vehicleno': "",
            'image1': "",
            'image2': "",
            'image3': "",
            'description': "",
            'rent': "",
        }
        widgets = {
            'vehiclename': forms.TextInput(attrs={'placeholder': 'Enter Vehicle Name'}),
            'capacity': forms.NumberInput(attrs={'placeholder': 'Enter Capacity'}),
            'vehicleno': forms.TextInput(attrs={'placeholder': 'Enter Vehicle Number'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'rent': forms.NumberInput(attrs={'placeholder': 'Enter Rent per day'}),
        }


