from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator

# Create your models here.

class Veterinary(Model):
    name = models.CharField(max_length=50)
    # name varchar(50)
    age = models.IntegerField(default=17, validators=[MinValueValidator(17)])