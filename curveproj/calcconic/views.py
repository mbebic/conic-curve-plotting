from django.shortcuts import render
import json
import logging
from django.http import HttpResponse, JsonResponse
from curveapp.models import conicselection
from curveapp.plotting import plot_conic
from django.contrib.auth.decorators import login_required, user_passes_test

from curveapp.views import is_member
# Create your views here.

# The subsequent decorators correctly protect the endpoint, but they 
# respond with a full page rather than a JSON object. 
# Handle in the calling function  as described here: https://stackoverflow.com/a/37121496

# We can also make a new function decorator as its own definition in this page
@login_required(login_url="login")
@user_passes_test(is_member, login_url="error")
def calculate(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        body = json.loads(request.body.decode('utf-8'))

        try:
            cid = int(body['id'])
            # logging.error("type of cid "+str(type(cid)))
            temp = conicselection.objects.get(pk=cid)
            # logging.error("temp %s" %(temp.a))
            points = plot_conic(temp.a, temp.b, temp.c, temp.d, temp.e, temp.f, Np=10)
            # logging.error("points %g" %(points['x'][0]))
            points['name'] = 'id %s' %cid
            return JsonResponse(points)
        
        except:
            return JsonResponse({'error': 'failed'})
                