from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weekly_availability = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)


class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weekly_availability = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
