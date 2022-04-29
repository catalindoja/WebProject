from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import *


class VeterinarySignupForm(UserCreationForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput, required=True)
    age = forms.IntegerField(required=True)
    address = forms.CharField(max_length=8, widget=forms.TextInput, required=True)
    postalcode = forms.IntegerField(required=True)
    zoo_id = forms.ModelChoiceField(queryset=Zoo.objects.all(), empty_label="(Nothing)")
    number_assigned_animals = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = WebUser


    @transaction.atomic
    def save(self):
        web_user = super().save(commit=False)
        web_user.is_veterinary = True
        web_user.save()

        veterinary = Veterinary.objects.create(User=web_user)
        print(self.data.get('number_assigned_animals'))
        print(veterinary.number_assigned_animals)
        veterinary.number_assigned_animals = self.data.get('number_assigned_animals')
        veterinary.name = self.data.get('name')
        veterinary.age = self.data.get('age')
        veterinary.address = self.data.get('address')
        veterinary.postalcode = self.data.get('postalcode')
        veterinary.zoo_id = self.data.get('zoo_id')
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print(veterinary.age)
        print(veterinary.postalcode)
        print(veterinary.number_assigned_animals)
        print(veterinary.name)
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        veterinary.save()
        print(veterinary.number_assigned_animals)
        # client.CIF.add(*self.cleaned_data.get('CIF'))
        return web_user  # web_user