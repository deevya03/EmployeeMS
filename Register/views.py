from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib import messages


def home(request):
    return render(request, 'base/base.html')


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("registerPage")

    else:
        form = RegistrationForm()
    return render(request=request, template_name="register/register.html", context={"register_form": form})
