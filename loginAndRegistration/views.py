from django.contrib              import messages
from django.contrib.auth.forms   import UserCreationForm
from django.shortcuts            import redirect, render
from django.contrib.auth         import authenticate, login
from loginAndRegistration.models import Doctor, Nurse, Patient
from dashboards.models           import Admin


def login_view(request):
    # Check if the register link was clicked go to register page
    if 'register' in request.GET:
        return redirect('register')
    
    # else process the login
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # User is valid
        if user is not None:
            login(request, user)
            if Admin.objects.filter(user=user).exists():
                return redirect('admin_home')
            elif Doctor.objects.filter(user=user).exists():
                return redirect('doctor_home')
            elif Nurse.objects.filter(user=user).exists(): # to make sure the user is a nurse
                messages.success(request, "Login Successful to Nurse Dashboard") # display message 
                return redirect('nurse_home') # go to nurse_home function in dashboards wiew.py
            elif Patient.objects.filter(user=user).exists():
                return redirect('patient_home')
        else:
            # if the User is not valid stay in login page and show the msg Invalid login credentials
            messages.error(request, "Invalid login credentials")
    
    return render(request, 'login.html')

def register(request):
    form = UserCreationForm()
    # context =
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
            messages.success(request, ("Registration Complete"))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})
