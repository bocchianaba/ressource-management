import logging
from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic

from clients.models import Client, Contract

# Create your views here.
# ...

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = "director/client.html"
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
        
        # Logger les valeurs de request.POST
        logger.info("Champs du formulaire : %s", request.POST)
        
        name = request.POST.get("nom")
        phone = request.POST.get("telephone")
        address = request.POST.get("adresse")
        email = request.POST.get("email")
        
        logger.info("le client qu'on essaye d'enregistrer a pour nom : %s, téléphone: %s, adresse: %s, email: %s",name, phone, address, email)
        
        client = Client(name=name, phone_number=phone, address=address, email=email)
        client.save()
        
    return HttpResponseRedirect(reverse("clients:index"))

def delete(request, id):
    try:
        element = Client.objects.get(id=id)
    except Client.DoesNotExist:
        logger.error("Le client avec l'identifiant %s n'existe pas.", id)
        raise Http404("Le client n'existe pas.")

    logger.info("Élément récupéré pour la suppression : %s", element)
    
    try:
        element.delete()
        logger.info("Suppression réussie de : %s", element)
    except Exception as e:
        logger.error("Une erreur s'est produite lors de la suppression du client avec l'identifiant %s : %s", id, str(e))
        # Gérer l'erreur ici, par exemple, afficher un message d'erreur à l'utilisateur ou rediriger vers une autre page

    return HttpResponseRedirect(reverse("clients:index"))


class ContractView(generic.ListView):
    template_name = "director/contract.html"
    context_object_name = "contracts_list"

    def get_queryset(self):
        """Return all the contract"""
        contracts = Contract.objects.all()
        logger.info("obtention de la liste des contrats. Les contrats créés sont au nombre de : %s", contracts.count())
        return contracts.reverse()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter la liste des clients au contexte
        context['clients_list'] = Client.objects.all()
        return context
    

def newContract(request):
    logger.info("création d'un nouveau contrat !")
    if(request.method=="POST"):
        
        logger.info("Méthode Post reçu")
        
        # Logger les valeurs de request.POST
        logger.info("Champs du formulaire : %s", request.POST)
        
        name = request.POST.get("name")
        client_id = request.POST.get("client")
        provider = request.POST.get("provider")
        description = request.POST.get("description")
        budget = request.POST.get("budget")
        duration = request.POST.get("duration")
        maxChanges = request.POST.get("maxChanges")
        
        logger.info("le contrat qu'on essaye d'enregistrer a pour nom : %s, id du client: %s, prestataire: %s, budget: %s, durée: %s, max de modif: %s, description %s, ", name, client_id, provider, budget, duration, maxChanges, description)
        
        # Récupérer l'objet client à partir de l'identifiant
        client = get_object_or_404(Client, pk=client_id)
        contract = Contract(name=name, client=client, description=description, provider=provider, budget=budget, duration=duration, max_changes=maxChanges)
        contract.save()
        
    return HttpResponseRedirect(reverse("clients:contracts"))