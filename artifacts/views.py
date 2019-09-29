from django.shortcuts import render
from .models import Artifact

# Create your views here.
def all_artifacts(request):
    artifacts = Artifact.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts})
    
"""
    def check_validity(start_time ,validity_period):
    if datetime.datetime.now() <= start_time + datetime.timedelta(hours=validy_period):
      return True
    return False
"""