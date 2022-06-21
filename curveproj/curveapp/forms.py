from django import forms
from django.forms import ModelForm
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from curveapp.models import conicselection

class conicForm(ModelForm):
    class Meta:
        model = conicselection
        fields = ['t', 'a', 'b', 'c', 'd', 'e', 'f']
