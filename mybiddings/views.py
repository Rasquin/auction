from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from artifacts.models import Artifact

# Create your views here.

@login_required()  
def view_my_biddings(request):
    """A View that renders the artifacts that the user has won"""
    artifacts = Artifact.objects.all()
    my_biddings = []
    user = request.session['username']
    
    for artifact in artifacts:
        if datetime.datetime.now() <= artifact.published_date + datetime.timedelta(hours=artifact.bidding_time):
           if user == artifact.by_user:
               artifact.price_to_pay == artifact.current_bidding_price
               my_biddings.append(artifact)
               
    return render(request, "mybiddings.html", {"my_biddings": my_biddings})