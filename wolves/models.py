from django.db import models

# Create your models here.
# models.py

class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    # Add more fields as needed
