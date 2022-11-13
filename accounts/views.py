from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import LoginForm, RegisterForm
from accounts.models import User


def superuser(user):
    return user.is_superuser


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('core:index')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@user_passes_test(superuser)
def users_view(request):
    user = User.objects.all()
    return render(request, 'accounts/users.html', {'users': user})


@user_passes_test(superuser)
def add_user_view(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data['password']
            permissions = form.cleaned_data['permissions']
            user = User.objects.create_user(email=email, password=password)
            user.user_permissions.set(permissions)
            return redirect('accounts:users')
    else:
        form = RegisterForm()
    return render(request, 'accounts/add_users.html', {'form': form})
