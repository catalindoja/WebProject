from django.urls import path, reverse
from . import views
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html',next_page='/home')),
    path('registration/register/', views.signup),
    path('list_data', views.list_data),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('registration/register_veterinary', SignupVeterinaryView.as_view(), name='registration/register_veterinary'),
    path('registration/register_staff', SignupStaffView.as_view(), name='registration/register_staff'),
    path('registration/register_visitor', SignupVisitorView.as_view(), name='registration/register_visitor'),
    path('create_animal', CreateAnimalView.as_view(), name='create_animal'),
    path('animal_editor/<str:pk>/', views.updateAnimal, name='edit/edit_animal'),
    path('animal_editor/', views.list_animals, name='animal_editor'),
    path('animal_delete/', views.list_animals_delete, name='animal_delete'),
    path('animal_delete/<str:pk>/', views.deleteAnimal, name='delete/delete_animal'),
    path('create_zoo', CreateZooView.as_view(), name='create_zoo'),

]

urlpatterns += staticfiles_urlpatterns()



