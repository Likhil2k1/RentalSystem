from django import forms
from .models import VehicleCustomer

class VehicleCustomerForm(forms.ModelForm):
    class Meta:
        model = VehicleCustomer
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


class SearchForm(forms.Form):
    type_choices = [('default','Select Type'),('Bike','BIKE'), ('Car','CAR')]
    type = forms.ChoiceField(choices=type_choices, label='')
    vehiclename = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Enter Vehicle Name'}))
    capacity = forms.IntegerField(required=True, label='', widget=forms.NumberInput(attrs={'placeholder':'Enter Capacity'}))                
