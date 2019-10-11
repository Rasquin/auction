from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import Artifact

# Create your views here.
def get_all_artifacts(request):
    artifacts = Artifact.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts})

def bidding_status(request, id):
    artifact = get_object_or_404(Artifact, pk=id)
    if datetime.datetime.now() <= artifact.published_date + datetime.timedelta(hours=artifact.bidding_time):
        artifact.on_bidding = True
    else:
        artifact.on_bidding = False
    return redirect(get_all_artifacts)

    
    """
    def bidding_status(request, pk):
    artifact = get_object_or_404(Artifact, pk=pk)
    if datetime.datetime.now() <= artifact.published_date + datetime.timedelta(hours=artifact.bidding_time):
        artifact.on_bidding = True
    else:
        artifact.on_bidding = False
    return redirect(get_all_artifacts)
    
def bidding_status(request, id):
    artifact = get_object_or_404(Artifact, pk=id)
    if datetime.datetime.now() <= artifact.published_date + datetime.timedelta(hours=artifact.bidding_time):
        artifact.on_bidding = True
    else:
        artifact.on_bidding = False
    return redirect(get_all_artifacts)
"""

def get_one_artifact(request, pk):
    the_artifact = get_object_or_404(Artifact, pk=pk)
    return render(request, "artifact.html", {"artifact": the_artifact})
    
    

"""

    def bidding_status(published_date ,validity_period):
    if datetime.datetime.now() <= published_date + datetime.timedelta(hours=bidding_time):
        on_bidding = True
        return artifact.on_bidding
    else
        on_bidding = False
    return artifact.on_bidding
    
    
    name = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    origin = models.CharField(max_length=200, default='')
    age = models.CharField(max_length=200, default='')
    description = models.TextField()
    crafting = models.TextField()
    trajectory = models.TextField()
    
    initial_price = models.DecimalField(max_digits=9, decimal_places=2)
    bidding_price = models.DecimalField(max_digits=9, decimal_places=2)
    buying_price = models.DecimalField(max_digits=9, decimal_places=2)
    
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    bidding_time = models.IntegerField(default=0)
    
    on_bidding = models.BooleanField(blank=False, default=True)
"""