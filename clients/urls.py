from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("/new", views.new, name="new"),
    path("/contrats", views.ContractView.as_view(), name="contracts"),
    path("/contrats/new", views.newContract, name="newContract"),
    path("/projets", views.ProjectView.as_view(), name="projects"),
    path("/projet/new", views.newProject, name="newProject"),
    path("/delete/<int:id>", views.delete, name="delete"),
    path("/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("/<int:pk>/contrats", views.IndexView.as_view(), name="index"),
]