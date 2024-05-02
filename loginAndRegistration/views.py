from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from loginAndRegistration.models import Doctor, Nurse, Patient
from django.contrib.auth import logout
from dashboards.models import Appointment
from dashboards.forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if Doctor.objects.filter(user=user).exists():
                return redirect('doctor_home')
            elif Nurse.objects.filter(user=user).exists():
                return redirect('nurse_home')
            elif Patient.objects.filter(user=user).exists():
                return redirect('patient_home')
            else:
                return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # info for automatic log in
            username = form.cleaned_data['username']
            # password 1 as two options for password
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Complete")
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')



def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('patient_home')
    else:
        form = AppointmentForm()

    return render(request, 'make_appointment.html', {'form': form})
