from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "name": "Edwin",
        "stack": "Django",
        "experience": "six months"
    }
    return render(request, "leads/index.html", context)
