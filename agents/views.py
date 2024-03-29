import random
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizerLoginRequiredMixin
from django.core.mail import send_mail


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
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f"{random.randint(0,10000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile,
        )

        send_mail(
            subject="You are invited to be an agent",
            message="You were created as an agent on DJCRM. Please login to start working.",
            from_email="admin@test.com",
            recipient_list=[user.email]
        )
        # accessing the specific user profile
        # agent.organization = self.request.user.userprofile
        # agent.save()  # saving to the database
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
