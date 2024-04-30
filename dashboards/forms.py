from django import forms
from .models import Appointment, Invoice
from dashboards.models import Prescription


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'nurse', 'appointment_date','appointment_time' 'status']

        


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['doctor', 'patient', 'issue_datetime', 'medication_details']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['patient', 'billing_datetime', 'amount', 'payment_status']


##class AppointmentForm(forms.Form):
  #  time_choices = [(f"{hour}:00", f"{hour}:00 - {hour+1}:00") for hour in range(9, 17)]
   # time = forms.ChoiceField(choices=time_choices)