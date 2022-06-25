from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
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

def is_member(user):
    return user.groups.filter(name="CircleGroup").exists()

@csrf_protect
@ensure_csrf_cookie
def index(request):
    if request.method == "POST":
        form = conicForm(request.POST)

        if form.is_valid():
            # form = conicForm.save()
            form.save()
            return render(request, 'curveapp/index.html', {
                "form": form
            })

    else:
        form = conicForm()

    return render(request, 'curveapp/index.html', {
        "form": form
    })

# @login_required(login_url="login")
# @user_passes_test(is_member, login_url="error")
@ensure_csrf_cookie
def library(request):
    return render(request, "curveapp/library.html", {
            "curvedata": conicselection.objects.all(),
            "permissions": user.get_group_permissions()
        })
    # if is_member(request.user, "CircleGroup"):
    #     return render(request, "curveapp/library.html", {
    #         "curvedata": conicselection.objects.all(),
    #     })
    # else:
    #     return render(request, "curveapp/error.html", {
    #         "message": "You are not authorized to view this page. Contact your supervisor to allow permissions."
    #     }) 

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