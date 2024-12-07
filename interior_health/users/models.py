# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('health_worker', 'Health Worker'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

