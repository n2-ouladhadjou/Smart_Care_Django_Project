from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from loginAndRegistration.models import Doctor, Nurse
from dashboards.forms import AppointmentForm, PrescriptionForm, InvoiceForm
from dashboards.models import Appointment, Prescription, Invoice
from django.contrib.auth.decorators import login_required


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
        if (self.request.user.groups.filter(name='admin').exists()):
            return self.request.user.groups.filter(name='admin').exists()
        else:
            return self.request.user.groups.filter(name='doctor').exists()

    def get(self, request, *args, **kwargs):
        if self.request.user.groups.filter(name='admin').exists():
            appointments = Appointment.objects.all()
            return render(request, 'manage_appointments.html', {'appointments': appointments})
        else:
            ## user is doctor
            current_user = request.user
            current_date = timezone.now().date()
            appointments = Appointment.objects.filter(doctor__user=current_user,
                                                      appointment_datetime__date=current_date)
            return render(request, 'manage_appointments.html', {'appointments': appointments})


def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)

    # Check if the appointment belongs to the current patient
    if appointment.patient == request.user.patient:
        # Delete the appointment
        appointment.delete()

    # Redirect back to the patient home page
    return redirect('patient_home')


@login_required()
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        appointment_datetime = request.POST.get('appointment_datetime')

        status = request.POST.get('status', 'Waiting for approval')
        if doctor_id != '':
            Appointment.objects.update(doctor=Doctor.objects.filter(id=doctor_id)[0],
                                       patient=request.user.patient,
                                       appointment_datetime=appointment_datetime,
                                       status=status)
        else:
            nurse_id = request.POST.get('nurse')
            Appointment.objects.update(
                nurse=Nurse.objects.filter(id=nurse_id),
                patient=request.user.patient,
                appointment_datetime=appointment_datetime,
                status=status
            )

        return redirect('patient_home')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'update_appointment.html', {'form': form, 'appointment': appointment, 'doctors': doctors})


class ManagePrescriptionsView(UserPassesTestMixin, View):
    def test_func(self):
        if self.request.user.groups.filter(name='admin').exists():
            return self.request.user.groups.filter(name='admin').exists()
        else:
            return self.request.user.groups.filter(name='doctor').exists()

    def get(self, request, *args, **kwargs):
        if (self.request.user.groups.filter(name='admin').exists()):
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
        invocie = Invoice.objects.all()
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


def patient_dashboard(request):
    # Retrieve the logged-in user
    user = request.user

    # Retrieve upcoming appointments for the patient
    appointments = Appointment.objects.filter(patient=user.patient_profile)

    # Pass the user and appointments to the template
    context = {
        'user': user,
        'appointments': appointments,
    }

    return render(request, 'patient.html', context)


def book_appointment(request):
    form = AppointmentForm(initial={'patient': request.user.patient_profile})
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or patient dashboard
            return redirect('patient_dashboard')
    return render(request, 'book_appointment.html', {'form': form})


def view_prescriptions(request):
    # Retrieve prescriptions for the logged-in patient
    prescriptions = Prescription.objects.filter(patient=request.user.patient_profile)
    return render(request, 'prescriptions.html', {'prescriptions': prescriptions})
