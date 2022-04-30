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