from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser


class WebUser(AbstractUser):
    is_veterinary = models.BooleanField(default=False)
    is_visitor = models.BooleanField(default=False)
    is_zoo_staff = models.BooleanField(default=False)


class Zoo(models.Model):
    zoo_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    max_visitors = models.DecimalField('Max amount of visitors', max_digits=8, decimal_places=0, blank=False, null=False)
    address = models.CharField(max_length=80)
    postalcode = models.DecimalField('Postal code', max_digits=8, decimal_places=0, blank=False, null=False)

    def __str__(self):
        return str(self.name)


class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    age = models.IntegerField(null=False)
    address = models.CharField(max_length=80)
    postalcode = models.IntegerField(blank=False, null=False)
    zoo_id = models.ForeignKey(Zoo, null=True, on_delete=models.CASCADE)
    # ??? phone_number = PhoneNumberField(null=False, blank=False, unique=True) # from phonenumber_field.modelfields import PhoneNumberField # pip install django-phonenumber-field
    # ??? zoo_id = get id from Zoo class

    def __str__(self):
        return str(self.name)


class Staff(Worker):
    User = models.OneToOneField(WebUser, on_delete=models.CASCADE, primary_key=True)
    assigned_habitat = models.CharField(max_length=80, default="Dolphins")

    def __str__(self):
        return str(self.User)


class Veterinary(Worker):
    User = models.OneToOneField(WebUser, on_delete=models.CASCADE, primary_key=True)
    number_assigned_animals = models.IntegerField(null=False, blank=False)
    # name varchar(50)

    def __str__(self):
        return str(self.User)


class Animal(models.Model):
    animal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    zoo_id = models.ForeignKey(Zoo, null=True, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
    veterinary_id = models.ForeignKey(Veterinary, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Visitor(models.Model):
    User = models.OneToOneField(WebUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40,blank=False,null=False)
    telephone = models.DecimalField(max_digits=9, decimal_places=0, blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    age = models.DecimalField(max_digits=3, decimal_places=0, blank=False,null=False)
    dateLatestVisit = models.DateField(default=date.today,blank=False,null=False)
    zoo_id = models.ForeignKey(Zoo, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.User)
