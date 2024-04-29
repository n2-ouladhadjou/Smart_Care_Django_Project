from django.contrib.auth.mixins     import UserPassesTestMixin
from django.views                   import View
from django.shortcuts               import render
from django.contrib.auth.decorators import login_required
from django.shortcuts               import render, redirect, get_object_or_404
from .models                        import Appointment

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

class ManageAppointmentsView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        # Add your logic here
        return render(request, 'manage_appointments.html')

class AdminView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        return render(request, 'admin.html')

class ManageUsersView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        # Add your logic here
        return render(request, 'admin.html')

class ManagePrescriptionsView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        # Add your logic here
        return render(request, 'manage_prescriptions.html')

class ManageInvoicesView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        # Add your logic here
        return render(request, 'manage_invoices.html')

class MangeUsersView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        # Add your logic here
        return render(request, 'manage_users.html')