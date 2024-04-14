import logging
from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic

from clients.models import Client, Contract, Project

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required



# Create your views here.
# ...

logger = logging.getLogger(__name__)

# @login_required
# class IndexView(generic.ListView):
#     template_name = "director/client.html"
#     context_object_name = "clients_list"

#     def get_queryset(self):
#         """Return all the clients"""
#         clients = Client.objects.all()
#         logger.info("obtention de la liste des clients. Les clients créés sont au nombre de : %s", clients.count())
#         return clients.reverse()
    
@login_required
def index_view(request):
    """Vue pour afficher la liste des clients."""
    clients = Client.objects.all()
    logger.info("Obtention de la liste des clients. Les clients créés sont au nombre de : %s", clients.count())
    context = {'clients_list': clients}
    return render(request, 'director/client.html', context)

@login_required
def LoginView(request):
    template_name = "auth/index.html"
    return render(request, template_name, None)
    # context_object_name = "clients_list"

    # def get_queryset(self):
    #     """Return all the clients"""
    #     clients = Client.objects.all()
    #     logger.info("obtention de la liste des clients. Les clients créés sont au nombre de : %s", clients.count())
    #     return clients.reverse()

@login_required
def DetailView():
    model = Client
    template_name = "director/detail.html"

@login_required
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

@login_required
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


@login_required
def ContractView(request):
    template_name = "director/contract.html"
    
    """Return all the contract"""
    contracts = Contract.objects.all()
    logger.info("obtention de la liste des contrats. Les contrats créés sont au nombre de : %s", contracts.count())
    
    # Ajouter la liste des clients au contexte
    clients = Client.objects.all()
    
    context = {'clients_list': clients.reverse(), 'contracts_list': contracts.reverse()}
    return render(request, template_name, context)

@login_required
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

@login_required
def ProjectView(request):
    template_name = "director/project.html"
    # context_object_name = "projects_list"
    
    """Return all the project"""
    projects = Project.objects.all()
    context = { 'projects_list': projects.reverse}
    logger.info("obtention de la liste des projets. Les contrats créés sont au nombre de : %s", projects.count())
    
    return render(request, template_name, context)


@login_required
def projectList(request):
    template_name = "project-manager/index.html"
    # context_object_name = "projects_list"
    
    """Return all the project"""
    projects = Project.objects.all()
    context = { 'projects_list': projects.reverse}
    logger.info("obtention de la liste des projets. Les contrats créés sont au nombre de : %s", projects.count())
    
    return render(request, template_name, context)


def newProject(request):
    logger.info("création d'un nouveau projet !")
    if(request.method=="POST"):
        
        logger.info("Méthode Post reçu")
        
        # Logger les valeurs de request.POST
        logger.info("Champs du formulaire : %s", request.POST)
        
        name = request.POST.get("nom")
        dueDate = request.POST.get("delai")
        description = request.POST.get("description")
        budget = request.POST.get("budget")
        
        logger.info("le contrat qu'on essaye d'enregistrer a pour nom : %s, budget: %s, deadline: %s, description %s, ", name, budget, dueDate, description)
        
        project = Project(name=name, deadline=dueDate, description=description, budget=budget)
        project.save()
        
    return HttpResponseRedirect(reverse("clients:projects"))


def login_view(request):
    if request.method == 'POST':
        # Créer une instance du formulaire de connexion et le remplir avec les données de la requête
        # form = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                if request.user.groups.filter(name='Director').exists():
                    return HttpResponseRedirect(reverse("clients:index"))
                elif request.user.groups.filter(name='Project Manager').exists():
                    return HttpResponseRedirect(reverse("clients:projectsList"))
            # Redirection vers une page après la connexion réussie
            return redirect('index')
        else:
            # Afficher un message d'erreur si l'authentification échoue
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    # else:
    #     # Afficher le formulaire de connexion vide
    #     form = LoginForm()
    return HttpResponseRedirect(reverse("login"))

def logout_view(request):
    if request.method=='POST':
        pass
        # logout()

    return HttpResponseRedirect(reverse("login"))
