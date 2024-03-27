"""
URL configuration for samrtCare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from dashboards.views import ManageUsersView, ManageAppointmentsView, ManagePrescriptionsView, ManageInvoicesView, \
    AdminView, delete_user, edit_appointment, delete_appointment, edit_prescription, delete_prescription
from dashboards import views as dashboard_views  # import dashboards views


from loginAndRegistration import views as auth_views
from django.urls import include, path



urlpatterns = [
    path('', core_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register, name='register'),
    path("/", include("django.contrib.auth.urls")),
    path('manage-users/', ManageUsersView.as_view(), name='manage_users'),
    path('edit-user/<int:user_id>/', dashboard_views.edit_user, name='edit_user'),  # use dashboards views
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('edit-appointment/<int:appointment_id>/', edit_appointment, name='edit_appointment'),
    path('delete-appointment/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    path('manage-appointments/', ManageAppointmentsView.as_view(), name='manage_appointments'),
    path('manage-prescriptions/', ManagePrescriptionsView.as_view(), name='manage_prescriptions'),
    path('manage-invoices/', ManageInvoicesView.as_view(), name='manage_invoices'),
    path('user-admin/', AdminView.as_view(), name='admin'),
    path('edit-prescription/<int:prescription_id>/', edit_prescription, name='edit_prescription'),
    path('delete-prescription/<int:prescription_id>/', delete_prescription, name='delete_prescription'),
    path('edit-invoice/<int:invoice_id>/', dashboard_views.edit_invoice, name='edit_invoice'),
    path('delete-invoice/<int:invoice_id>/', dashboard_views.delete_invoice, name='delete_invoice'),
]