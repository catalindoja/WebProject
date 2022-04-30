from django.contrib import admin
from zooproject import models
# Register your models here.
admin.site.register(models.Zoo)
admin.site.register(models.Animal)
admin.site.register(models.Worker)
admin.site.register(models.Staff)
admin.site.register(models.Veterinary)
admin.site.register(models.Visitor)
admin.site.register(models.WebUser)
