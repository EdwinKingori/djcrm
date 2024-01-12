from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:pk>", views.lead_detail, name="lead_detail"),
    path("create/", views.CreateLead, name='createlead')
]
