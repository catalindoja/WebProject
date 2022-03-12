from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from veterinary.models import Veterinary


def index(request):
    veterinary = Veterinary.objects.all()

    #list_veterinary = ", ".join([veterinary.name for veterinary in veterinarians])
    #return HttpResponse(list_veterinary)
    #return HttpResponse("OK");

    json = {'veterinary':veterinary}
    return render(request,'veterinary/index.html',json)
