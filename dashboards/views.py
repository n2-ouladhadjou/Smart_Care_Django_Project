from django.contrib.auth.forms      import UserChangeForm
from django.contrib.auth.mixins     import UserPassesTestMixin
from django.contrib.auth.models     import User
from django.http                    import HttpResponseRedirect
from django.urls                    import reverse
from django.views                   import View
from django.shortcuts               import render, get_object_or_404, redirect
from django.utils                   import timezone
from datetime                       import datetime
from dashboards.forms               import AppointmentForm, PrescriptionForm, InvoiceForm, CustomUserChangeForm
from dashboards.models              import Appointment, Prescription, Invoice
from django.contrib.auth.decorators import login_required

# Function to display the oppontments in nurse dashboard
@login_required
def nurse_home(request):
    return render(request, 'nurseDashboard.html',  {'appointments' : Appointment.objects.all()})

# Function to update the oppontments status in nurse dashboard and save it in database
@login_required
def update_appointment_status(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        if request.POST.get('status') == 'completed':
            appointment.status = 'Completed'
            appointment.save()
        elif request.POST.get('status') == 'canceled':
            appointment.status = 'Canceled'
            appointment.save()
    return redirect('nurse_home')

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
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = CustomUserChangeForm(instance=user)
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
            appointments = Appointment.objects.filter(doctor__user=current_user, appointment_datetime__date=current_date)
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
