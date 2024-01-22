from django.urls import path

from . import views

urlpatterns = [
    path('', views.AgentListView.as_view(), name='agents'),
    path('<int:pk>', views.AgentDetailView.as_view(), name="agent_detail"),
    path("<int:pk>/update/", views.UpdateAgentView.as_view(), name="update"),
    path("<int:pk>/delete/", views.DeleteAgentView.as_view(), name="delete"),
    path('create/', views.CreateAgentView.as_view(), name='createagent'),

]
