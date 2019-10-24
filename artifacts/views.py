from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from decimal import Decimal
from datetime import datetime, timedelta
from .models import Artifact

# Create your views here.
def get_all_artifacts(request):
    """
    Get the list of artifacts that are in the auction
    """
    artifacts = Artifact.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts})

def bidding_status(request, id):
    """
    Define if an aritfact is or not for auction
    """
    artifact = get_object_or_404(Artifact, pk=id)
    if datetime.datetime.now() <= artifact.published_date + datetime.timedelta(hours=artifact.bidding_time):
        artifact.on_bidding = True
    else:
        artifact.on_bidding = False
    return redirect(get_all_artifacts)

    
def get_one_artifact(request, pk):
    """
    Get the info of one particular artifact
    """
    the_artifact = get_object_or_404(Artifact, pk=pk)
    
    if the_artifact.current_bidding_price <= Decimal(0.5)*the_artifact.expert_value:
        the_artifact.buy_now_price = round(Decimal(0.75)*the_artifact.expert_valuex,2)
        #messages.error(request, "buying price 0.75 of expert_value!")
    
    elif Decimal(0.5)*the_artifact.expert_value < the_artifact.current_bidding_price < the_artifact.expert_value:
        the_artifact.buy_now_price = round(Decimal(2)*the_artifact.current_bidding_price,2)
        #messages.error(request, "buying price 2 of current bid!")
    
    else:
        the_artifact.buy_now_price = round(Decimal(1.5)*the_artifact.current_bidding_price,2)
        #messages.error(request, "buying price 1.5 of current bid")
    
    the_artifact.save()
    
    return render(request, "artifact.html", {"artifact": the_artifact})
    

def get_buy_now_price (request, id):
    """
    Define the price to buy the artifact inmediately.
    Depending on the current_bidding_price & expert_value the buy_now_price change
    """
    the_artifact = get_object_or_404(Artifact, pk=id)
    
    if the_artifact.current_bidding_price <= Decimal(0.5)*the_artifact.expert_value:
        the_artifact.buy_now_price = round(Decimal(0.75)*the_artifact.expert_valuex,2)
        #messages.error(request, "buying price 0.75 of expert_value!")
    
    elif Decimal(0.5)*the_artifact.expert_value < the_artifact.current_bidding_price < the_artifact.expert_value:
        the_artifact.buy_now_price = round(Decimal(2)*the_artifact.current_bidding_price,2)
        # messages.error(request, "buying price 2 of current bid!")
    
    else:
        the_artifact.buy_now_price = round(Decimal(1.5)*the_artifact.current_bidding_price,2)
        #messages.error(request, "buying price 1.5 of current bid")
    
    the_artifact.price_to_pay = the_artifact.buy_now_price
    the_artifact.save()
        
    return {"artifact": the_artifact}