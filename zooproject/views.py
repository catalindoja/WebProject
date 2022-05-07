# Create your views here.
from django.contrib.auth import login, authenticate
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
    template_name = 'register_animal.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_veterinary:
            return redirect('/')
        else:
            form = self.form_class
            template_name = 'register_animal.html'
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


def list_animals_delete(request):
    if request.user.is_veterinary:
        animals = Animal.objects.all()
        animals_dictionary = {'animals': animals}
        return render(request, 'zooproject/list_animals2.html', animals_dictionary)
    else:
        print("Error el user no es un veterinario")
        return redirect('/')

def deleteAnimal(request, pk):
    animal = Animal.objects.get(animal_id=pk)
    if request.user.is_veterinary:
        if request.method == 'POST':
            animal.delete()
            return redirect('/animal_delete')
        context = {'item':animal}
        return render(request, 'delete/delete_animal.html', context)
    else:
        print("Error el user no es un veterinario")
        return redirect('/')




'''
class PeticionStandClienteView(CreateView):
    model = PeticionStand
    form_class = PeticionStandClienteForm
    template_name = 'peticion_stand_cliente.html'

    def form_valid(self, form):
        if self.request.user.is_client:
            client = Cliente.objects.get(User=self.request.user)
            form.instance.clientUsername = client
            form.save()
            return redirect('lista_peticiones_cliente')
        else:
            print("Error, user is not a client")
            return redirect('/')


def peticionStandGestorList(request, key):
    if request.user.is_gestor:
        peticiones = PeticionStand.objects.all()
        arr_peticiones = []
        for peticion in peticiones:
            if peticion.revisado is False and peticion.idEvento == Event.objects.get(id=key):
                arr_peticiones.append(peticion)
        dictionary = {'peticiones': arr_peticiones}
        return render(request, 'lista_peticiones_stand.html', dictionary)
    else:
        print("Error el user no es un gestor")
        return redirect('/')


def updatePeticionStandGestor(request, pk):
    if request.user.is_gestor:
        peticion = PeticionStand.objects.get(id=pk)
        form = PeticionStandGestorForm(instance=peticion)

        if request.method == 'POST':
            form = PeticionStandGestorForm(request.POST, instance=peticion)
            gestores = Gestor.objects.all()
            my_gestor = None
            for g in gestores:
                if g.User.username == request.user.username:
                    my_gestor = g
            form.instance.gestorUsername = my_gestor
            if form.is_valid():
                if form.instance.estado is True:
                    stand = Stand.objects.get(id=form.instance.idStand.id)
                    stand.occupied = True
                    stand.save()
                form.save()
                return redirect('lista_stands_revisados')

        context = {'form':form}
        return render(request, 'peticion_stand_gestor.html', context)
    else:
        print("Error el user no es un gestor")
        return redirect('/')


def listaPeticionesCliente(request):
    if request.user.is_client:
        peticiones = PeticionStand.objects.all()
        arr_peticiones = []
        for peticion in peticiones:
            if peticion.clientUsername == Cliente.objects.get(User=request.user):
                if peticion.estado is True and peticion.revisado is True:
                    peticion.estado_peticion = 'Aceptada'
                elif peticion.revisado is True and peticion.estado is False:
                    peticion.estado_peticion = 'Denegada'
                else:
                    peticion.estado_peticion = 'Pendiente de revision'
                arr_peticiones.append(peticion)
        dictionary = {'peticiones': arr_peticiones}
        return render(request, 'lista_peticiones_cliente.html', dictionary)
    else:
        print("Error el user no es un cliente")
        return redirect('/')

'''