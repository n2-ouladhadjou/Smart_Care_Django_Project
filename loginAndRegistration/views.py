from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            messages.success(request, ("Log in Complete"))
            return redirect('home')
        else:
            # Return an error message or handle authentication failure
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html')


def register(request):
    form= UserCreationForm()
    #context = 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #info for automatic log in
            username=form.cleaned_data['username']
            #password 1 as two options for password
            password=form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, ("Registration Complete"))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html',{'form':form})
