from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator
from datetime import date


class Zoo(models.Model):
    zoo_id = models.AutoField(primary_key=True)
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
    age = models.DateField(default=date.today, blank=False, null=False)
    address = models.CharField(max_length=80)
    postalcode = models.DecimalField('Postal code', max_digits=8, decimal_places=0, blank=False, null=False)
    # ??? phone_number = PhoneNumberField(null=False, blank=False, unique=True) # from phonenumber_field.modelfields import PhoneNumberField # pip install django-phonenumber-field
    # ??? zoo_id = get id from Zoo class

    def __unicode__(self):
        return u"%s" % self.name


class Staff(Worker):
    staff_id = models.AutoField(primary_key=True)
    assigned_habitat = models.CharField(max_length=80, default="Dolphins")

    def __unicode__(self):
        return u"%s" % self.name


class Veterinary(Worker):
    vet_id = models.AutoField(primary_key=True)
    assigned_animals = models.IntegerField(null=False, blank=False)
    # name varchar(50)


    def __unicode__(self):
        return u"%s" % self.name


class Visitor(models.Model):
    name = models.CharField(max_length=40,blank=False,null=False)
    telephone = models.DecimalField(max_digits=9, decimal_places=0, blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    age = models.DecimalField(max_digits=3, decimal_places=0, blank=False,null=False)
    dateLatestVisit = models.DateField(default=date.today,blank=False,null=False)
    latestZooVisited = models.IntegerField(blank=False,null=False)

    def __unicode__(self):
        return u"%s" % self.name