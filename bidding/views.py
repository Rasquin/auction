from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from artifacts.models import Artifact
from artifacts.views import get_one_artifact

# Create your views here.

@login_required()
def place_bidding(request, id):
    "Place a new bidding on an artifact"
    
    the_artifact = get_object_or_404(Artifact, pk=id)
    new_bidding =  Decimal(request.POST.get('new_bidding'))
    
   # if the_artifact.current_bidding_price < the_artifact.minimun_bidding_price:
    #    messages.error(request, "Your bid is not high enough")
    #else:
    if the_artifact.current_bidding_price >= new_bidding:
        messages.error(request, "Your bid is not high enough")
            
    else:
        if new_bidding < the_artifact.minimun_bidding_price:
            messages.error(request, "Your bid is not higher than the minimun amount to bid")
        else:
            the_artifact.current_bidding_price = new_bidding
            the_artifact.by_user = request.user.id
            the_artifact.save()
            messages.error(request, "Your bid has been successfully placed !")

    return redirect('/artifacts/' + id)
