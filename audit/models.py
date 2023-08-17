from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class APICall(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)     # The authenticated user who made the API call
    endpoint = models.CharField(max_length=255)                  # The endpoint of the API call (e.g., "/api/some-endpoint")
    method = models.CharField(max_length=10)                      # The HTTP method used for the API call (e.g., "GET", "POST")
    timestamp = models.DateTimeField(auto_now_add=True)            # The timestamp when the API call was made (automatically set to the current time when the object is created)
    ip_address = models.GenericIPAddressField(null=False, default='0.0.0.0')# The IP address of the client who made the API call
    extra_data = models.JSONField( blank=True, null=True)        #This JSONField named "extra_data"  allowing it to store additional data as a JSON object, and permitting the field to be left blank or set to null if not provided.       
    
    # By setting null=False and providing a default value of '0.0.0.0', it ensures that an IP address is always present