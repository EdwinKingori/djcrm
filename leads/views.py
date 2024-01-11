from django.shortcuts import render
from . models import Lead
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
