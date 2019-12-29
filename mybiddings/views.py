from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from artifacts.models import Artifact

# Create your views here.

@login_required()  
def view_my_biddings(request):
    """A View that renders the artifacts that the user has won"""
    artifacts = Artifact.objects.all()
    users = User.objects.all()
    immeditely_bought_artifacts = []
    auction_won_artifacts = []
    my_biddings = []
    current_user_id = request.user.id
    
    for artifact in artifacts:
        if artifact.paid:
            if current_user_id == artifact.by_user:
               immeditely_bought_artifacts.append(artifact)
        else:
            if timezone.now() >  artifact.end_date:
               if current_user_id == artifact.by_user:
                   artifact.price_to_pay == artifact.current_bidding_price
                   auction_won_artifacts.append(artifact)
            else:
                if current_user_id == artifact.by_user:
                   my_biddings.append(artifact)
                   print(my_biddings)

    return render(request, "mybiddings.html", {"immeditely_bought_artifacts": immeditely_bought_artifacts, "auction_won_artifacts": auction_won_artifacts, "my_biddings": my_biddings})