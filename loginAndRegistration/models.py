from django.db import models
from django.contrib.auth.models import User
from datetime import date



class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weekly_availability = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weekly_availability = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Patient(models.Model):

    title_choices = {
        "Master" : "Master",
        "Mr" : "Mr",
        "Miss" : "Miss",
        "Mrs" : "Mrs",
        "Dr" : "Dr"
    }
    patienttype_choices = {
        "Not Registered" : "Not Registered",
        "Private" : "Private",
        "NHS" : "NHS"
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=10, choices=title_choices)
    name = models.CharField(blank=True, max_length=60)
    address = models.CharField(blank=True,max_length=255)
    dob = models.DateField(blank=True, null=True, default=date.today)
    contact_info = models.CharField(blank=True, max_length=25)
    patienttype = models.CharField(blank=True, max_length=15, choices=patienttype_choices)

    def __str__(self):
        return self.user.username
