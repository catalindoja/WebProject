from django.urls import path, reverse

from . import views
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]

urlpatterns += staticfiles_urlpatterns()



