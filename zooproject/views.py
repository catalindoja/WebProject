# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Worker


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


class RegisterView(TemplateView):
    template_name = 'register.html'
