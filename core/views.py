from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.contrib.auth.models import Group


def home(request):
    user = request.user
    # Probaly more efficient way of doing this switch etc but there are only 4 options so not too bad atm
    # assumes user is only assigned to one group type
    if(user.groups.filter(name='Patient').exists()):
        return render(request, 'patientDashboard.html')
    if(user.groups.filter(name='Doctor').exists()):
        return render(request, 'doctor.html')
        #return render(request, 'doctorDashboard.html')   
    if(user.groups.filter(name='Nurse').exists()):
        return render(request, 'nurseDashboard.html')
    if(user.groups.filter(name='Admin').exists()):
        return render(request, 'admin.html')
        #return render(request, 'adminDashboard.html')
    
    # default view for no user set, could be changed to patient?
    return render(request, 'home.html')
