from django import forms
from django.contrib.auth.models import User

from .models import Appointment, Invoice
from dashboards.models import Prescription
from django.contrib.auth.forms import UserChangeForm
from django import forms


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'nurse', 'patient', 'appointment_datetime', 'status']


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['doctor', 'patient', 'issue_datetime', 'medication_details']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['patient', 'billing_datetime', 'amount', 'payment_status']


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
