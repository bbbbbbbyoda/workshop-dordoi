from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserAuthenticationForm
from .models import MyUser


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'account/register.html', {'form': form})
    form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})


def authentication_view(request):
    if request.method == "POST":
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password')
            user = authenticate(request, phone_number=phone_number, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'index' with your desired URL

            form.add_error('password', 'Не правильный пароль или номер телефона')

            return render(request, 'account/authentication.html', {'form': form})
        else:
            return render(request, 'account/authentication.html', {'form': form})
    else:
        form = UserAuthenticationForm()

    return render(request, 'account/authentication.html', {'form': form})


@login_required(login_url='/register/')
def logout_view(request):
    logout(request)
    return redirect('index')
