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
