from django.db import models
from django.contrib.auth.models import User

# Create your models here.


BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class Donor(models.Model):

    
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group=models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    phone_number=models.CharField(max_length=15)
    address=models.TextField()
    availability=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} ({self.blood_group})"


class Patient(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group_needed=models.CharField(max_length=3,choices=BLOOD_GROUP_CHOICES)
    phone_number=models.CharField(max_length=15)
    address=models.TextField()
    request_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} needs {self.blood_group_needed}"
