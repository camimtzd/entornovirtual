from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    Project = Project.objects.all()
    return render(request,"portfolio/portfolio.html",{'Project':Project})