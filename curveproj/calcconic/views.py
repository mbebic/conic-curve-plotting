from django.shortcuts import render
import json
import logging
from django.http import HttpResponse, JsonResponse
from curveapp.models import conicselection
from curveapp.plotting import plot_conic
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# Protecting an API endpoint by a custom-defined permission.
@login_required(login_url="login")
@permission_required('calcconic.can_calc_conics', raise_exception=True)
def calculate(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        body = json.loads(request.body.decode('utf-8'))

        try:
            cid = int(body['id'])
            # logging.error("type of cid "+str(type(cid)))
            temp = conicselection.objects.get(pk=cid)
            # logging.error("temp %s" %(temp.a))
            points = plot_conic(temp.a, temp.b, temp.c, temp.d, temp.e, temp.f) # Np=10
            # logging.error("points %g" %(points['x'][0]))
            points['name'] = 'id %s' %cid
            return JsonResponse(points)
        
        except:
            return JsonResponse({'error': 'failed'})
