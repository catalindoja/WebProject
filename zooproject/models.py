from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Zoo(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    max_visitors = models.DecimalField('Max amount of visitors', max_digits=8, decimal_places=0, blank=False, null=False)
    address = models.CharField(max_length=80)
    postalcode = models.DecimalField('Postal code', max_digits=8, decimal_places=0, blank=False, null=False)

    def __unicode__(self):
        return u"%s" % self.name


class Animal(models.Model):
    animal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    #zoo_id = get id from Zoo class
    #caretaker_id = get id from Staff class
    #veterinary_id = get id from Veterinary class

    def __unicode__(self):
        return u"%s" % self.name


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    occupation = models.CharField(max_length=15)
    address = models.CharField(max_length=80)
    postalcode = models.DecimalField('Postal code', max_digits=8, decimal_places=0, blank=False, null=False)
    # ??? phone_number = PhoneNumberField(null=False, blank=False, unique=True) # from phonenumber_field.modelfields import PhoneNumberField # pip install django-phonenumber-field
    # ??? zoo_id = get id from Zoo class

    def __unicode__(self):
        return u"%s" % self.name