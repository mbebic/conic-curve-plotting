from django import forms
from django.forms import ModelForm
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from curveapp.models import circleinput, ellipseinput, conicselection

class circleForm(ModelForm):
    class Meta:
        model = circleinput
        fields = ['circle_x', 'circle_y', 'circle_radius']

class ellipseForm(ModelForm):
    class Meta:
        model = ellipseinput
        fields = ['ellipse_x', 'ellipse_y', 'ellipse_a',
                    'ellipse_b', 'ellipse_rot']

class conicForm(ModelForm):
    class Meta:
        model = conicselection
        fields = ['a', 'b', 'c', 'd', 'e', 'f']
