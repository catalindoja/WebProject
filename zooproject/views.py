# Create your views here.
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView



class SignupVeterinaryView(CreateView):
    model = WebUser
    form_class = VeterinarySignupForm
    template_name = 'registration/register_veterinary.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'veterinary'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        web_user = form.save()
        login(self.request, web_user)
        return redirect('/')


class SignupStaffView(CreateView):
    model = WebUser
    form_class = StaffSignupForm
    template_name = 'registration/register_staff.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'zoo_staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        web_user = form.save()
        login(self.request, web_user)
        return redirect('/')


class SignupVisitorView(CreateView):
    model = WebUser
    form_class = VisitorSignupForm
    template_name = 'registration/register_visitor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'visitor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        web_user = form.save()
        login(self.request, web_user)
        return redirect('/')


class CreateAnimalView(CreateView):
    model = Animal
    form_class = CreateAnimalForm
    template_name = 'create_animal.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_veterinary:
            return redirect('/')
        else:
            form = self.form_class
            template_name = 'create_animal.html'
            return render(request, template_name, {'form': form})

    def form_valid(self, form):
        if self.request.user.is_veterinary:
            veterinary = Veterinary.objects.get(User=self.request.user)
            form.instance.veterinary_id = veterinary
            form.save()
            return redirect('/')

        else:
            print("Error, user is not a veterinary")
            return redirect('/')



class CreateZooView(CreateView):
    model = Zoo
    form_class = CreateZooForm
    template_name = 'create_zoo.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect('/')
        else:
            form = self.form_class
            template_name = 'create_zoo.html'
            return render(request, template_name, {'form': form})

    def form_valid(self, form):
        if self.request.user.is_superuser:
            admin = get_user_model()
            form.instance.Username = admin
            form.save()
            return redirect('/')
        else:
            print("Error, user is not an admin")
            return redirect('/')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def list_data(r):
    workers = Worker.objects.all()
    workers_dictionary =  {'workers': workers}
    
    return render(r, 'zooproject/list_data.html', workers_dictionary)


def list_animals(request):
    if request.user.is_veterinary:
        animals = Animal.objects.all()
        animals_dictionary = {'animals': animals}
        return render(request, 'zooproject/list_animals.html', animals_dictionary)
    else:
        print("Error el user no es un veterinario")
        return redirect('/')

def updateAnimal( request, *args, **kwargs):
    if request.user.is_veterinary:
        animal = Animal.objects.get(animal_id=kwargs.get('pk'))
        form = AnimalEditorForm(instance=animal)

        if request.method == 'POST':
            form = AnimalEditorForm(request.POST, instance=animal)
            form.instance.animal_id = kwargs.get('pk')
            if form.is_valid():
                edit_animal = Animal.objects.get(animal_id=kwargs.get('pk'))
                edit_animal.save()
                form.save()
                return redirect('/animal_editor')

        context = {'form': form}
        return render(request, 'edit/edit_animal.html', context)
    else:
        print("Error el user no es un veterinario")
        return redirect('/')

def deleteAnimal(request, pk):
    animal = Animal.objects.get(animal_id=pk)
    if request.user.is_veterinary:
        if request.method == 'POST':
            animal.delete()
            return redirect('/animal_editor')
        context = {'item':animal}
        return render(request, 'delete/delete_animal.html', context)
    else:
        print("Error el user no es un veterinario")
        return redirect('/')


def home(request):
    return render(request, 'home.html')


def logout(request):
    return redirect('/')
