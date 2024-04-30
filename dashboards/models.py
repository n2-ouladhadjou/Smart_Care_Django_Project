from django.contrib.auth.models import User
from django.db import models
from datetime import date,time, datetime, timedelta

from loginAndRegistration.models import Doctor, Nurse, Patient


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField(blank=True,null=True)
    status = models.CharField(max_length=255)


class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    issue_datetime = models.DateTimeField()
    medication_details = models.TextField()


class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    billing_datetime = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=255)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
