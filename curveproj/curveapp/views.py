from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from django import forms
import plotly.graph_objects as go

from .forms import conicForm
from .models import conicselection

# Create your views here.

@csrf_protect
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

# import json
# import numpy as np
# def makexy(a,b,c,d,e,f):
#     # do the work here - create x, y numpy arrays as practiced in jupyter
#     # for now creating just a sinewave
#     x=np.linspace(0,2*np.pi,100)
#     y = np.sin(x)
#     temp = {'x': x.tolist(), 'y':y.tolist()}

#     return json.dumps(temp, indent=2)

# def curveplotdata():
#     return 

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

def testlookup(request, curve_id):
    curve = conicselection.objects.get(pk=curve_id)

def library(request):
    return render(request, "curveapp/library.html", {
        "curvedata": conicselection.objects.all(),
    })

