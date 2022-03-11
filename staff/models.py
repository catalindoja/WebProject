from email.policy import default
from django import forms
from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator
# Create your models here.

class Staff(Model):
    name = models.CharField(max_length=50)
    # name varchar(50)
    age = models.IntegerField(default=17, validators=[MinValueValidator(17)])
    # Create your models here.
