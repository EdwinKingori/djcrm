from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import Lead, Agent
from .forms import LeadForm
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
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        # Checking if form is valid
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            print("Lead created Successfully!")
            return HttpResponseRedirect(reverse("index"))
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)
