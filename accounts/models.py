from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Make email unique so two users cannot share the same email
    email = models.EmailField(unique=True, blank=False, null=False)
    
    # You can add custom fields here later if needed (e.g., phone number, bio)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username