import logging
from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic

from clients.models import Client

# Create your views here.
# ...

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = "director/index.html"
    context_object_name = "clients_list"

    def get_queryset(self):
        """Return all the clients"""
        clients = Client.objects.all()
        logger.info("obtention de la liste des clients. Les clients créés sont au nombre de : %s", clients.count())
        return clients.reverse()
    


class DetailView(generic.DetailView):
    model = Client
    template_name = "director/detail.html"

def new(request):
    logger.info("création d'un nouveau client !")
    if(request.method=="POST"):
        
        logger.info("Méthode Post reçu")
        
        name=request.POST["nom"]
        phone=request.POST["telephone"]
        address=request.POST["adresse"]
        email=request.POST["email"]
        
        logger.info("le client qu'on essaye d'enregistrer a pour nom : %s, téléphone: %s, adresse: %s, email: %s",name, phone, address, email)
        
        client = Client(name=name, phone_number=phone, address=address, email=email)
        client.save()
        
    return HttpResponseRedirect(reverse("clients:index"))