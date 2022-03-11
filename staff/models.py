from email.policy import default
import imp
from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator
from utils_classes.dni import DNIField

# Create your models here.

class Staff(Model):
    nif = DNIField()
    name = models.CharField(max_length=50)
    # name varchar(50)
    age = models.IntegerField(default=17, validators=[MinValueValidator(17)])
    # Create your models here.
