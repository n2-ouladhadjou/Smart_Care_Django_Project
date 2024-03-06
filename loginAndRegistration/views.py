from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('home')
        else:
            # Return an error message or handle authentication failure
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html')


def register(request):
    return render(request, 'registration.html')
