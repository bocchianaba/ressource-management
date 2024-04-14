from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("/new", views.new, name="new"),
    path("/delete/<int:id>", views.delete, name="delete"),
    path("/<int:pk>/", views.DetailView.as_view(), name="detail"),
]