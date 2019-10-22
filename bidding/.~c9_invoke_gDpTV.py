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
    #quantity = int(request.POST.get('quantity'))
    
    if the_artifact.current_bidding_price >= new_bidding:
        messages.error(request, "Your bid is not high enough")
    
    else:
        the_artifact.current_bidding_price = new_bidding
        the_artifact.save()
        messages.error(request, "Your bid has been successfully placed !")
    
    return redirect(reverse('index'))
    #return redirect(get_one_artifact(request,id))
    #return  render(request, "artifact.html", {"artifact": the_artifact})
    


    

"""

from decimal import Decimal
Decimal(request.POST.get('whatever'))

def add_to_cart(request, id):
    "Add a quantity of the specified product to the cart"
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    
    if id in cart:
        #If the item is already in the cart, you want to add the new quantity to the existing quantity. 
        cart[id] = int(cart[id]) + quantity      
    else:
        #However, if the item is not in the cart, then the current add_to_cart view works.
        cart[id] = cart.get(id, quantity) 


    request.session['cart'] = cart
    return redirect(reverse('index'))# the products.hml is called index

"""