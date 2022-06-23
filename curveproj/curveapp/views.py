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

def conicgraph(request):
    x = [-2,0,4,6,7]
    y = [q**2-q+3 for q in x]
    x1 = [-3,1,5,7,9]
    y1 = [2*q**2-q-1 for q in x1]
    trace = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10},
                        mode="lines",  name='1st Trace')

    trace1 = go.Scatter(x=x1, y=y1, marker={'color': 'blue', 'symbol': 104, 'size': 10},
                        mode="lines",  name='2nd Trace')

    layout=go.Layout(title="Meine Daten", xaxis={'title':'x'}, yaxis={'title':'y'})
    figure=go.Figure(data=[trace, trace1],layout=layout)

    return render(request, 'curveapp/conicgraph.html', {
        "graph": figure.to_html()
    })

# def testlookup(request, curve_id):
#     curve = conicselection.objects.get(pk=curve_id)

@ensure_csrf_cookie
def library(request):
    return render(request, "curveapp/library.html", {
        "curvedata": conicselection.objects.all(),
    })

