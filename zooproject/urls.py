from django.urls import path, reverse
from . import views
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html',next_page='/list_data')),
    path('registration/register/', views.signup),
    path('list_data', views.list_data),
    path('registration/register_veterinary', SignupVeterinaryView.as_view(), name='registration/register_veterinary')
]

urlpatterns += staticfiles_urlpatterns()



