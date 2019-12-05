from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
#from datetime import datetime, timedelta
from artifacts.models import Artifact

# Create your views here.

@login_required()  
def view_my_biddings(request):
    """A View that renders the artifacts that the user has won"""
    artifacts = Artifact.objects.all()
    users = User.objects.all()
    auction_won_artifacts = []
    my_biddings = []
    current_user_id = request.user.id
    
    for artifact in artifacts:
        if timezone.now() >  artifact.end_date:
        #if datetime.now() >=  datetime.now() + timedelta(hours=10):
        #if datetime.datetime.now() <= artifact.published_date + datetime.timedelta(hours=artifact.bidding_time):
           if current_user_id == artifact.by_user:
               artifact.price_to_pay == artifact.current_bidding_price
               auction_won_artifacts.append(artifact)
        else:
            if current_user_id == artifact.by_user:
               my_biddings.append(artifact)

    return render(request, "mybiddings.html", {"auction_won_artifacts": auction_won_artifacts}, {"my_biddings": my_biddings})
    
    
    
    
    
    
    """
    the field in the model - 
user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="artifactuser")
    """