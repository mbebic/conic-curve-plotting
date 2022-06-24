from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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


@ensure_csrf_cookie
def library(request):
    return render(request, "curveapp/library.html", {
        "curvedata": conicselection.objects.all(),
    })

