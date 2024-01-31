from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("<int:pk>", views.LeadDetailView.as_view(), name="lead_detail"),
    path("<int:pk>/update/", views.UpdateLeadView.as_view(), name="update"),
    path("<int:pk>/delete/", views.LeadDeleteView.as_view(), name="delete"),
    path("<int:pk>/assign-agent/",
         views.AssignAgentView.as_view(), name='assign-agent'),
    path("create/", views.CreateLeadView.as_view(), name='createlead'),
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view(),
         name="category-detail"),

]
