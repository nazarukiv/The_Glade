from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import login as auth_login
from users.forms import UserLoginForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()

    context = {
        'title': 'Authorization',
        'form': form
    }

    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Registration'
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Profile'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    pass