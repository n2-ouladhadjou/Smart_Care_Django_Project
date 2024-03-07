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

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField()
    status = models.CharField(max_length=255)

class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    issue_datetime = models.DateTimeField()
    medication_details = models.TextField()

class Invoice(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    billing_datetime = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=255)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Collaboration(models.Model):
    partner_gp = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurse_operation_exchange = models.BooleanField()

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Turnover(models.Model):
    week_start_date = models.DateField()
    week_end_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class AddressLookup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
