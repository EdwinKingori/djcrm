from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import Lead, Agent
from .forms import LeadForm, LeadModelForm
# Create your views here.


def index(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/index.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


def CreateLead(request):

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        # Checking if form is valid
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = LeadModelForm()

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


def update_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        # Checking if form is valid
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = LeadModelForm()

    context = {
        "form": form,
        "lead": lead
    }

    return render(request, "leads/update_lead.html", context)

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
