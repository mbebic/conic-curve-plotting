from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Permission
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.urls import reverse
from django import forms
import plotly.graph_objects as go

from .forms import conicForm
from .models import conicselection

# Create your views here.

# This function illustrates usage of user_passes_test decorator
# addapted from: https://stackoverflow.com/a/20110261
def is_calcconic_sub(user):
    return user.groups.filter(name="calcconic-subscribers").exists()

@csrf_protect
@ensure_csrf_cookie
def index(request):
    if request.method == "POST":
        form = conicForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'curveapp/index.html', {
                "form": form
            })

    else:
        form = conicForm()

    return render(request, 'curveapp/index.html', {
        "form": form
    })

@login_required(login_url="login")
@user_passes_test(is_calcconic_sub, login_url="error")
@ensure_csrf_cookie
def library(request):
    return render(request, "curveapp/library.html", {
            "curvedata": conicselection.objects.all(),
            # "permissions": Permission.objects.filter(user=request.user)
        }) 

def error_page(request):
    return render(request, "curveapp/error.html", {
            "message": "You are not authorized to view this page. Contact your supervisor to allow permissions."
        }) 

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            # return render(request, "curveapp/index.html")
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "curveapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "curveapp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def welcome(request):
    return render(request, 'curveapp/welcome.html')