from django.db import models
from datetime import date

# Create your models here.
class Visitor(models.Model):
    Name = models.CharField(max_length=40,blank=False,null=False)
    Telephone = models.DecimalField(max_digits=9, decimal_places=0, blank=False,null=False)
    Email = models.EmailField(blank=False,null=False)
    Age = models.DecimalField(max_digits=3, decimal_places=0, blank=False,null=False)
    DateLatestVisit = models.DateField(default=date.today,blank=False,null=False)
    LatestZooVisited = models.IntegerField(blank=False,null=False)
