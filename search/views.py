from django.shortcuts import render
from artifacts.models import Artifact

# Create your views here.
def search_by_name(request):
    artifacts = Artifact.objects.filter(name__icontains=request.GET['q']) # for some reaseon dont want to get by artifact_name
    return render(request, "artifacts.html", {"artifacts": artifacts})

def filters(request):
    artifacts = Artifact.objects.filter(name__icontains=request.GET['q'])
    return render(request, "artifacts.html", {"artifacts": artifacts})