from django.urls import path
from . import views

urlpatterns = [
    path("apps", views.applications_list, name="applications_list"),
    path("apps/new", views.add_application, name="add_application"),
    path("apps/<int:pk>/edit", views.edit_application, name="edit_application"),
    path("apps/<int:pk>/delete", views.delete_application, name="delete_application"),
    path("dashboard", views.dashboard, name="dashboard"),

]
