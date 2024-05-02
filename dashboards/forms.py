from django import forms
from .models import Appointment, Invoice
from dashboards.models import Prescription


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
