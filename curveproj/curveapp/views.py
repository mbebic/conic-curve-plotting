from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from django import forms

from .forms import conicForm
from .models import circleinput, ellipseinput

# Create your views here.
# def index(request):
#     return render(request, 'curveapp/index.html')

@csrf_protect
def index(request):
    if request.method == "POST":
        form = conicForm(request.POST)

        if form.is_valid():
            # form = conicForm.save()
            form.save()
            return render(request, 'curveapp/index.html')

    else:
        form = conicForm()

    return render(request, 'curveapp/index.html', {
        "form": form
    })