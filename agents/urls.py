from django.urls import path

from . import views

urlpatterns = [
    path('', views.AgentListView.as_view(), name='agents'),
    path('<int:pk>', views.AgentDetailView.as_view(), name="agent_detail"),
    path('create/', views.CreateAgentView.as_view(), name='createagent'),

]
