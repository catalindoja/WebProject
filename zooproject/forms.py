from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from django.forms import ModelForm

from .models import *
import datetime


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
        zoo = Zoo.objects.get(zoo_id=self.data.get('zoo_id'))
        veterinary = Veterinary.objects.create(
            User=web_user, postalcode=self.data.get('postalcode'),
            zoo_id=zoo, number_assigned_animals= self.data.get('number_assigned_animals'),
            name=self.data.get('name'), address = self.data.get('address'),
            age=self.data.get('age'))
        veterinary.save()
        # client.CIF.add(*self.cleaned_data.get('CIF'))
        return web_user  # web_user


class StaffSignupForm(UserCreationForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput, required=True)
    age = forms.IntegerField(required=True)
    address = forms.CharField(max_length=8, widget=forms.TextInput, required=True)
    postalcode = forms.IntegerField(required=True)
    zoo_id = forms.ModelChoiceField(queryset=Zoo.objects.all(), empty_label="(Nothing)")
    assigned_habitat = forms.CharField(max_length=80, widget=forms.TextInput, required=True)

    class Meta(UserCreationForm.Meta):
        model = WebUser

    @transaction.atomic
    def save(self):
        web_user = super().save(commit=False)
        web_user.is_zoo_staff = True
        web_user.save()
        zoo = Zoo.objects.get(zoo_id=self.data.get('zoo_id'))
        staff = Staff.objects.create(
            User=web_user, postalcode=self.data.get('postalcode'),
            zoo_id=zoo, assigned_habitat= self.data.get('assigned_habitat'),
            name=self.data.get('name'), address = self.data.get('address'),
            age=self.data.get('age'))
        staff.save()
        # client.CIF.add(*self.cleaned_data.get('CIF'))
        return web_user  # web_user


class AnimalSignupForm(ModelForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput, required=True)
    zoo_id = forms.ModelChoiceField(queryset=Zoo.objects.all(), empty_label="(Nothing)")
    staff_id = forms.ModelChoiceField(queryset=Staff.objects.all(), empty_label="(Nothing)")
    veterinary_id = forms.ModelChoiceField(queryset=Veterinary.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = Animal
        exclude = ['']

    @transaction.atomic
    def save(self):
        web_user = super().save(commit=False)
        web_user.is_veterinary = True
        web_user.save()
        zoo = Zoo.objects.get(zoo_id=self.data.get('zoo_id'))
        staff = Staff(self.data.get('staff_id'))
        veterinary = Veterinary(self.data.get('veterinary_id'))
        animal = Animal.objects.create(
            zoo_id=zoo,
            staff_id=staff,
            veterinary_id=veterinary,
            name=self.data.get('name'))
        animal.save()
        # client.CIF.add(*self.cleaned_data.get('CIF'))
        return web_user  # web_user


class VisitorSignupForm(UserCreationForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput, required=True)
    telephone = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)
    dateLatestVisit = forms.DateField(initial=datetime.date.today)
    zoo_id = forms.ModelChoiceField(queryset=Zoo.objects.all(), empty_label="(Nothing)")

    class Meta(UserCreationForm.Meta):
        model = WebUser

    @transaction.atomic
    def save(self):
        web_user = super().save(commit=False)
        web_user.is_visitor = True
        web_user.save()
        zoo = Zoo.objects.get(zoo_id=self.data.get('zoo_id'))
        visitor = Visitor.objects.create(
            User=web_user, telephone=self.data.get('telephone'), email= self.data.get('email'),
            age=self.data.get('age'), dateLatestVisit=self.data.get('dateLatestVisit'), zoo_id=zoo)
        visitor.save()
        # client.CIF.add(*self.cleaned_data.get('CIF'))
        return web_user  # web_user

class AnimalEditorForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ['animal_id']
'''

class PeticionStandClienteForm(forms.ModelForm):
    class Meta:
        model = PeticionStand
        exclude = ['clientUsername', 'gestorUsername', 'estado', 'revisado']


class PeticionStandGestorForm(forms.ModelForm):
    class Meta:
        model = PeticionStand
        exclude = ['gestorUsername']

'''