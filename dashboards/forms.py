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


from django.contrib.auth.models import Group

from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserChangeForm
from django.contrib.admin.widgets import FilteredSelectMultiple


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=FilteredSelectMultiple("Groups", is_stacked=False),
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'groups')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['groups'].queryset = Group.objects.exclude(id__in=self.instance.groups.values_list('id', flat=True))
