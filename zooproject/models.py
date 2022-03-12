from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# TODO: check comments with ???
# TODO: get occupation from another class (veterinary or staff)?
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