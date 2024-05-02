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
    AdminView, view_prescriptions, book_appointment, patient_dashboard, delete_user, update_appointment, \
    delete_appointment, edit_prescription, delete_prescription
from dashboards import views as dashboard_views  # import dashboards views

from loginAndRegistration import views as auth_views
from django.urls import include, path

urlpatterns = [
    # path("/", include("django.contrib.auth.urls")),
    path('', core_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register, name='register'),
    path('user_logout/', auth_views.user_logout, name='user_logout'),
    path('manage-users/', ManageUsersView.as_view(), name='manage_users'),
    path('edit-user/<int:user_id>/', dashboard_views.edit_user, name='edit_user'),  # use dashboards views
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('manage-prescriptions/', ManagePrescriptionsView.as_view(), name='manage_prescriptions'),
    path('manage-invoices/', ManageInvoicesView.as_view(), name='manage_invoices'),
    path('user-admin/', AdminView.as_view(), name='admin'),
    path('edit-invoice/<int:invoice_id>/', dashboard_views.edit_invoice, name='edit_invoice'),
    path('delete-invoice/<int:invoice_id>/', dashboard_views.delete_invoice, name='delete_invoice'),

    # Prescription
    path('create_prescription/<int:appointment_id>/', core_views.create_prescription, name='create_prescription'),
    path('update_prescription/<int:prescription_id>/', core_views.update_prescription, name='update_prescription'),
    path('view_prescription/<int:prescription_id>/', core_views.view_prescription, name='view_prescription'),

    # Patient
    path('book_appointment/', book_appointment, name='book_appointment'),

    path('patient_home/', core_views.patient_home, name='patient_home'),
    path('delete_appointment/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    path('update_appointment/<int:appointment_id>/', update_appointment, name='update_appointment'),
    path('repeat-appointment/', core_views.repeat_appointment, name='repeat_appointment'),

    # Doctor
    path('doctor_home/', core_views.doctor_home, name='doctor_home'),

    path('approve_appointment/<int:appointment_id>/', core_views.approve_doctor_appointment,
         name='approve_appointment'),
    path('update_doctor_appointment/<int:appointment_id>/', core_views.update_doctor_appointment,
         name='update_doctor_appointment'),
    path('reject_appointment/<int:appointment_id>/', core_views.reject_doctor_appointment, name='reject_appointment'),

    # Nurse
    path('approve_nurse_appointment/<int:appointment_id>/', core_views.approve_doctor_appointment,
         name='approve_appointment'),
    path('update_nurse_appointment/<int:appointment_id>/', core_views.update_doctor_appointment,
         name='update_doctor_appointment'),
    path('reject_nurse_appointment/<int:appointment_id>/', core_views.reject_doctor_appointment,
         name='reject_appointment'),
]
