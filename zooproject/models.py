from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Animal(models.Model):
    animal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    #zoo_id = get id from Zoo class
    #caretaker_id = get id from Staff class
    #veterinary_id = get id from Veterinary class

def __unicode(self):
    return u"%s" % self.name