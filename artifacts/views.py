from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from decimal import Decimal
from django.utils import timezone
from .models import Artifact

# Create your views here.
def get_all_artifacts(request):
    """
    Get the list of artifacts that are currently at the  auction
    """
    the_artifacts = Artifact.objects.all()
    artifacts = []
    
    for artifact in the_artifacts:
        if timezone.now() <  artifact.end_date:
            artifact.on_bidding = True
            artifact.save()
            artifacts.append(artifact)
        else:
            artifact.on_bidding = False
            artifact.save()

    return render(request, "artifacts.html", {"artifacts": artifacts})

"""def bidding_status(request, id):
    """
    #Define if an aritfact is or not for auction
    
"""
    artifact = get_object_or_404(Artifact, pk=id)
    if datetime.datetime.now() <= artifact.published_date + datetime.timedelta(hours=artifact.end_date):
        artifact.on_bidding = True
    else:
        artifact.on_bidding = False
    return redirect(get_all_artifacts)
"""
    
def get_one_artifact(request, pk):
    """
    Get the info of one particular artifact
    """
    the_artifact = get_object_or_404(Artifact, pk=pk)
    users = User.objects.all()
    
   
    if the_artifact.current_bidding_price <= Decimal(0.5)*the_artifact.expert_value:
        the_artifact.buy_now_price = round(Decimal(0.75)*the_artifact.expert_value,2)
        #messages.error(request, "buying price 0.75 of expert_value!")
    
    elif Decimal(0.5)*the_artifact.expert_value < the_artifact.current_bidding_price < the_artifact.expert_value:
        the_artifact.buy_now_price = round(Decimal(2)*the_artifact.current_bidding_price,2)
        #messages.error(request, "buying price 2 of current bid!")
    
    else:
        the_artifact.buy_now_price = round(Decimal(1.5)*the_artifact.current_bidding_price,2)
        #messages.error(request, "buying price 1.5 of current bid")
    
    the_artifact.save()
    

    for user in users:
        if the_artifact.by_user == user.id:
            the_user = user
    
    return render(request, "artifact.html", {"artifact": the_artifact}, {"user": the_user})
    

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