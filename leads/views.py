from typing import Any
from django.core.mail import send_mail
from django.db.models.query import QuerySet
# from django.contrib.auth.forms import
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizerLoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
# Create your views here.


# Creating a signup view class
class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

# def landing_page(request):
#     return render(request, "landing.html")


class LandingPageView(TemplateView):
    template_name = "landing.html"


# def index(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads": leads
#     }
#     return render(request, "leads/index.html", context)
class IndexView(LoginRequiredMixin, ListView):
    template_name = "leads/index.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user

        # initial queryset  of leads for the entire organization
        if user.is_organizer:
            # if the user is an organizer, then they have a user profile(acessed through user.userprofile in the database)
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            # else if they are not an organizer, being an agent, we filter the agent through the current organization
            queryset = Lead.objects.filter(
                organization=user.agent.organization)
            # filtering the leads based on the agents field, where the agent has the user equal to user which is, self.reqest.user
            queryset = queryset.filter(agent__user=user)
        return queryset


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead
#     }
#     return render(request, "leads/lead_detail.html", context)
class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    # queryset = Lead.objects.all()
    model = Lead
    context_object_name = "lead"


# def CreateLead(request):

#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         # Checking if form is valid
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("index"))
#     else:
#         form = LeadModelForm()

#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)
class CreateLeadView(OrganizerLoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("index")

    def form_valid(self, form):
        # To Send e-mail
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(CreateLeadView, self).form_valid(form)


# def update_lead(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)

#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         # Checking if form is valid
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("index"))
#     else:
#         form = LeadModelForm()

#     context = {
#         "form": form,
#         "lead": lead
#     }

#     return render(request, "leads/update_lead.html", context)
class UpdateLeadView(OrganizerLoginRequiredMixin, UpdateView):
    template_name = "leads/update_lead.html"
    model = Lead
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("index")


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return HttpResponseRedirect(reverse("index"))


class LeadDeleteView(OrganizerLoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    model = Lead

    def get_success_url(self):
        return reverse("index")


# Manual update function
# def update_lead(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             Lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()

#             return HttpResponseRedirect(reverse('index'))
#     context = {
#         "form": form,
#         "lead": lead
#     }

#     return render(request, "leads/update_lead.html", context)


# def CreateLead(request):

#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         # Checking if form is valid
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = form.cleaned_data['agent']
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )

#             return HttpResponseRedirect(reverse("index"))
#     else:
#         form = LeadModelForm()

#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)
