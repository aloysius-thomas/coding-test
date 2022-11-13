from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from accounts.forms import LoginForm


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})





