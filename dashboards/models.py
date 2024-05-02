from django.contrib.auth.models  import User
from django.db                   import models
from django.utils.timezone       import now
from loginAndRegistration.models import Doctor, Nurse, Patient

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField(default = now, verbose_name = 'oppontement time')
    # Status can be Pending or Completed or canceled
    status  = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ), default='pending')
    def __str__(self): # change the name in database
        return self.patient.user.get_full_name()

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
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
