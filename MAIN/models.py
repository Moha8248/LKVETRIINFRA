from django.db import models

class LandRequest(models.Model):
    client_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    
    # User address fields
    user_door_no = models.CharField(max_length=100)
    user_area = models.CharField(max_length=100)  # Changed city to area
    user_district = models.CharField(max_length=100)
    user_state = models.CharField(max_length=100)
    user_country = models.CharField(max_length=100)
    
    # Land address fields
    land_area = models.CharField(max_length=100)  # Changed city to area
    land_district = models.CharField(max_length=100)
    land_state = models.CharField(max_length=100)
    land_country = models.CharField(max_length=100)
    
    land_required_sqft = models.IntegerField()
    additional_details = models.TextField()

    def __str__(self):
        return self.client_name
