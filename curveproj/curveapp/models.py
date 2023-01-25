from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import Max
from django.forms import ModelForm

# Create your models here
class conicselection(models.Model):
    # t designates type of curve: 1 is circle, 2 is ellipse
    t = models.IntegerField()
    # conic specified as: ax^2 + bxy + cy^2 + dx + ey + f = 0
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    e = models.FloatField()
    f = models.FloatField()

    def __str__(self):
        temp = 'Circle' if self.t == 1 else 'Ellipse'
        return '%s' %(temp)
        # return '%s (a,b,c,d,e,f): (%g, %g, %g, %g, %g, %g)' %(temp, self.a, self.b, self.c, self.d, self.e, self.f)

    def cvalues(self):
        return '(a,b,c,d,e,f): (%g, %g, %g, %g, %g, %g)' %(self.a, self.b, self.c, self.d, self.e, self.f)