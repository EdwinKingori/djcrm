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
        agent = form.save(commit=False)
        # accessing the specific user profile
        agent.organization = self.request.user.userprofile
        # Check if UserProfile exists, create if not (method 2)
        # user_profile, created = UserProfile.objects.get_or_create(
        #     user=self.request.user)
        # agent.organization = user_profile
        agent.save()
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
