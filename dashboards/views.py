from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import JsonResponse

from dashboards.forms import AppointmentForm, PrescriptionForm, InvoiceForm
from dashboards.models import Appointment, Prescription, Invoice
from loginAndRegistration.models import Patient


class AdminView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        return render(request, 'admin.html')


class ManageUsersView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'manage_users.html', {'users': users})


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})


def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('manage_users')


def get(request, *args, **kwargs):
    # Add your logic here
    return render(request, 'manage_appointments.html')


class ManageAppointmentsView(UserPassesTestMixin, View):
    def test_func(self):
        ## change this to decorator function?
        ## or use built in permission system with the permissions applied to the group
        if(self.request.user.groups.filter(name='admin').exists()):
            return self.request.user.groups.filter(name='admin').exists()
        else:
            return self.request.user.groups.filter(name='doctor').exists()

    def get(self, request, *args, **kwargs):
        if(self.request.user.groups.filter(name='admin').exists()):
            appointments = Appointment.objects.all()
            return render(request, 'manage_appointments.html', {'appointments': appointments})
        else:
            ## user is doctor
            current_user = request.user
            current_date = timezone.now().date()
            appointments = Appointment.objects.filter(doctor__user=current_user, appointment_date=current_date)
            return render(request, 'manage_appointments.html', {'appointments': appointments})            


def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    return redirect('manage_appointments')


def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('manage_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'edit_appointment.html', {'form': form})


class ManagePrescriptionsView(UserPassesTestMixin, View):
    def test_func(self):
        if(self.request.user.groups.filter(name='admin').exists()):
            return self.request.user.groups.filter(name='admin').exists()
        else:
            return self.request.user.groups.filter(name='doctor').exists()

    def get(self, request, *args, **kwargs):
        if(self.request.user.groups.filter(name='admin').exists()):
            prescription = Prescription.objects.all()
            return render(request, 'manage_prescriptions.html', {'prescriptions': prescription})
        else:
            ## user is doctor
            current_user = request.user
            prescription = Prescription.objects.filter(doctor__user=current_user)
            return render(request, 'manage_prescriptions.html', {'prescriptions': prescription})              


def edit_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('manage_prescriptions')
    else:
        form = PrescriptionForm(instance=prescription)
    return render(request, 'edit_prescription.html', {'form': form})


def delete_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    prescription.delete()
    return redirect('manage_prescriptions')


class ManageInvoicesView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        invocie= Invoice.objects.all()
        return render(request, 'manage_invoices.html', {'invoices': invocie})


def edit_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('manage_invoices')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'edit_invoice.html', {'form': form})


def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoice.delete()
    return redirect('manage_invoices')










#Patient Stuff

def patient_dashboard(request):
    # Retrieve patient information based on the current user
    patient = Patient.objects.get(user=request.user)
    context = {
        'patient': patient
    }
    return render(request, 'patient_dashboard.html', context)

def book_appointment(request):

    today = datetime.now().date()
    current_week = [today + timedelta(days=day) for day in range(0, 7)]
    next_week = [today + timedelta(days=7+day) for day in range(0, 7)]
    range_slots = ['{}:00 - {}:00'.format(slot, slot + 1) for slot in range(9, 17)]
    context = {
            'current_week': current_week,
            'next_week': next_week,
            'range_slots': range_slots,
        }
    return render(request, 'book_appointment.html', context)

def view_prescriptions(request):
    # Retrieve prescriptions for the logged-in patient
    prescriptions = Prescription.objects.filter(patient=request.user.patient)
    return render(request, 'view_prescriptions.html', {'prescriptions': prescriptions})


