from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganizerLoginRequiredMixin
from leads.models import Agent, UserProfile
from .forms import AgentModelForm
# Create your views here.


class AgentListView(OrganizerLoginRequiredMixin, generic.ListView):
    template_name = "agents/agents_list.html"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class CreateAgentView(OrganizerLoginRequiredMixin, generic.CreateView):
    template_name = "agents/create_agent.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents")

    def form_valid(self, form):
        # Commit false ensures agent is not saved in the database
        agent = form.save(commit=False)
        # accessing the specific user profile
        agent.organization = self.request.user.userprofile
        agent.save()  # saving to the database
        return super(CreateAgentView, self).form_valid(form)


class AgentDetailView(OrganizerLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class UpdateAgentView(OrganizerLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents")

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class DeleteAgentView(OrganizerLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"

    def get_success_url(self):
        return reverse("agents")

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
