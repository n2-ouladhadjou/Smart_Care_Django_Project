from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from dashboards.models import Appointment
from loginAndRegistration.models import Doctor, Nurse, Patient
from dashboards.forms import AppointmentForm, PrescriptionForm
from dashboards.models import Prescription


def home(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'patient'):
            return redirect('patient_home')
        elif hasattr(request.user, 'doctor'):
            return redirect('doctor_home')
        elif hasattr(request.user, 'nurse'):
            return redirect('nurse_home')
        else:
            return render(request, 'home.html')

    return render(request, 'home.html')


@login_required()
def patient_home(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        nurse_id = request.POST.get('nurse')
        appointment_datetime = request.POST.get('appointment_datetime')
        status = "Waiting for approval"

        if doctor_id != '':
            doctor = Doctor.objects.filter(id=doctor_id)[0]
            Appointment.objects.create(doctor=doctor,
                                       patient=request.user.patient,
                                       appointment_datetime=appointment_datetime,
                                       status=status)
        else:
            nurse = Nurse.objects.filter(id=nurse_id)
            Appointment.objects.create(
                nurse=nurse,
                patient=request.user.patient,
                appointment_datetime=appointment_datetime,
                status=status
            )

    # Retrieve past appointments
    past_appointments = Appointment.objects.filter(patient=request.user.patient,
                                                   status='Completed',
                                                   )
    # Loop through past completed appointments and get associated prescriptions
    for appointment in past_appointments:
        appointment.prescription = Prescription.objects.filter(appointment=appointment).first()

    # Retrieve upcoming appointments
    upcoming_approved_appointments = Appointment.objects.filter(patient=request.user.patient,
                                                                status='Approved',
                                                                )

    # Retrieve appointments needing approval
    pending_appointments = Appointment.objects.filter(patient=request.user.patient,
                                                      status='Waiting for approval',
                                                      )
    doctors = Doctor.objects.all()
    nurses = Nurse.objects.all()
    context = {
        'past_appointments': past_appointments,
        'upcoming_approved_appointments': upcoming_approved_appointments,
        'pending_appointments': pending_appointments,
        'doctors': doctors,
        'nurses': nurses,
    }

    return render(request, 'patient_home.html', context)


@login_required()
def doctor_home(request):
    doctor = request.user.doctor
    past_completed_appointments = Appointment.objects.filter(doctor=doctor,
                                                             status='Completed', )
    # Loop through past completed appointments and get associated prescriptions
    for appointment in past_completed_appointments:
        appointment.prescription = Prescription.objects.filter(appointment=appointment).first()

    upcoming_appointments = Appointment.objects.filter(doctor=doctor,
                                                       status='Approved',
                                                       )
    pending_appointments = Appointment.objects.filter(doctor=doctor,
                                                      status='Waiting for approval')

    context = {
        'past_completed_appointments': past_completed_appointments,
        'upcoming_appointments': upcoming_appointments,
        'pending_appointments': pending_appointments,
    }

    return render(request, 'doctor_home.html', context)


@login_required()
def nurse_home(request):
    nurse = request.user.nurse
    past_completed_appointments = Appointment.objects.filter(nurse=nurse,
                                                             status='Completed',
                                                             appointment_datetime__lt=timezone.now())
    upcoming_appointments = Appointment.objects.filter(nurse=nurse,
                                                       status='Approved',
                                                       appointment_datetime__gte=timezone.now())
    pending_appointments = Appointment.objects.filter(nurse=nurse,
                                                      status='Waiting for approval')

    context = {
        'past_completed_appointments': past_completed_appointments,
        'upcoming_appointments': upcoming_appointments,
        'pending_appointments': pending_appointments,
    }

    return render(request, 'nurse_home.html', context)


@login_required()
def approve_doctor_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            appointment.status = 'Approved'
            appointment.save()
        elif action == 'reject':
            rejection_reason = request.POST.get('rejection_reason')
            appointment.status = 'Rejected'
            appointment.rejection_reason = rejection_reason
            appointment.save()
        return redirect('doctor_home')

    return render(request, 'doctor_home.html', {'appointment': appointment})


@login_required()
def reject_doctor_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    if request.method == 'POST':
        reason = request.POST.get('reason')

        # Set status to Rejected and add reason for rejection
        appointment.status = 'Rejected'
        appointment.rejection_reason = reason
        appointment.save()

        return redirect('doctor_home')  # Redirect to doctor's home page

    return render(request, 'doctor_reject_appointment.html', {'appointment': appointment})


@login_required()
def update_doctor_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if form.is_valid():
        form.save()
        return redirect('doctor_home')

    return render(request, 'doctor_update_appointment.html', {'form': form, 'appointment': appointment})


@login_required()
def approve_nurse_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            appointment.status = 'Approved'
            appointment.save()
        elif action == 'reject':
            rejection_reason = request.POST.get('rejection_reason')
            appointment.status = 'Rejected'
            appointment.rejection_reason = rejection_reason
            appointment.save()
        return redirect('nurse_home')

    return render(request, 'nurse_home.html', {'appointment': appointment})


@login_required()
def reject_nurse_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    if request.method == 'POST':
        reason = request.POST.get('reason')

        # Set status to Rejected and add reason for rejection
        appointment.status = 'Rejected'
        appointment.rejection_reason = reason
        appointment.save()

        return redirect('nurse_home')  # Redirect to doctor's home page

    return render(request, 'nurse_reject_appointment.html', {'appointment': appointment})


@login_required()
def update_nurse_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if form.is_valid():
        form.save()
        return redirect('doctor_home')

    return render(request, 'nurse_update_appointment.html', {'form': form, 'appointment': appointment})


@login_required
def create_prescription(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        Prescription.objects.create(
            appointment=appointment,
            doctor=request.user.doctor,
            patient=appointment.patient,
            issue_datetime=appointment.appointment_datetime,
            medication_details=request.POST.get('medication_details', 'No Prescription required')
        )
        # Mark the appointment as completed
        appointment.status = 'Completed'
        appointment.save()
        return redirect('doctor_home')
    else:
        form = PrescriptionForm()
    return render(request, 'create_prescription.html', {'form': form})


@login_required
def update_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('view_prescription', prescription_id=prescription_id)
    else:
        form = PrescriptionForm(instance=prescription)
    return render(request, 'update_prescription.html', {'form': form, 'prescription': prescription})


@login_required
def view_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    return render(request, 'view_prescription.html', {'prescription': prescription})


@login_required()
def repeat_appointment(request):
    from datetime import datetime
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        nurse_id = request.POST.get('nurse')
        appointment_datetime = datetime.strptime(request.POST.get('appointment_datetime').replace('.', ''), "%B %d, %Y, %I:%M %p")
        # Create a new appointment with the same details
        Appointment.objects.create(
            doctor_id=doctor_id,
            nurse_id=nurse_id,
            patient=request.user.patient,
            appointment_datetime=appointment_datetime,
            status="Waiting for approval"
        )
    return redirect('patient_home')
