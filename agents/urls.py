from django.urls import path

from . import views

urlpatterns = [
    path('', views.AgentListView.as_view(), name='agents'),
    path('create/', views.CreateAgentView.as_view(), name='createagent'),
]
