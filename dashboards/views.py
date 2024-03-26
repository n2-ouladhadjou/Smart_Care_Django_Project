from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from django.shortcuts import render
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


class ManageAppointmentsView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

    def get(self, request, *args, **kwargs):
        # Add your logic here
        return render(request, 'manage_appointments.html')

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