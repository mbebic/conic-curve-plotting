from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import Max
from django.forms import ModelForm

# Create your models here.
class circleinput(models.Model):
    circle_x = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000000)])
    circle_y = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000000)])
    circle_radius = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000000)])

    def __str__(self):
        return 'Circle: %d %d %d' %(self.circle_x, self.circle_y, self.circle_radius)

class ellipseinput(models.Model):
    ellipse_x = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000000)])
    ellipse_y = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000000)])
    ellipse_a = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000000)])
    ellipse_b = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000000)])
    ellipse_rot = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(360)])

    def __str__(self):
        return 'Ellipse: %d %d %d %d %d' %(self.ellipse_x, self.ellipse_y, self.ellipse_a, self.ellipse_b, self.ellipse_rot)


class conicselection(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    d = models.IntegerField()
    e = models.IntegerField()
    f = models.IntegerField()

    def __str__(self):
        return 'Info: %d %d %d %d %d %d' %(self.a, self.b, self.c, self.d, self.e, self.f)