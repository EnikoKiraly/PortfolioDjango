from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    skils = Skil.objects.all()
    timelines = Timeline.objects.all()
    projects = Project.objects.all()
    certifikates = Certificate.objects.all()
    context = {"skils":skils, "timelines":timelines,
               "projects":projects, "certifikates":certifikates}
    return render(request, 'portfolio/index.html', context)