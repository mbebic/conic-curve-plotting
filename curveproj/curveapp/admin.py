from django.contrib import admin
from .models import circleinput, conicselection, ellipseinput

# Register your models here.
admin.site.register(circleinput)
admin.site.register(ellipseinput)
admin.site.register(conicselection)