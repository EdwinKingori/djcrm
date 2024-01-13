from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:pk>", views.lead_detail, name="lead_detail"),
    path("<int:pk>/update/", views.update_lead, name="update"),
    path("<int:pk>/delete/", views.lead_delete, name="delete"),
    path("create/", views.CreateLead, name='createlead'),
]
