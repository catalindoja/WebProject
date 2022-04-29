from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import *


class VeterinarySignupForm(UserCreationForm):
    number_assigned_animals = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = Veterinary

    @transaction.atomic
    def save(self):
        web_user = super().save(commit=False)
        web_user.is_veterinary = True
        web_user.save()
        veterinary = Veterinary.objects.create(User=web_user)
        print(self.data.get('number_assigned_animals'))
        print(veterinary.number_assigned_animals)
        veterinary.number_assigned_animals = self.data.get('number_assigned_animals')
        veterinary.save()
        print(veterinary.number_assigned_animals)
        # client.CIF.add(*self.cleaned_data.get('CIF'))
        return web_user  # web_user