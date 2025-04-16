from django import forms
from .models import LandRequest

class LandRequestForm(forms.ModelForm):
    class Meta:
        model = LandRequest
        fields = [
            'client_name', 'mobile_number', 
            # User address fields
            'user_door_no', 'user_area', 'user_district', 'user_state', 'user_country', 
            # Land address fields
            'land_area', 'land_district', 'land_state', 'land_country', 
            'land_required_sqft', 'additional_details'
        ]
