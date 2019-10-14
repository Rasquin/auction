from django.shortcuts import get_object_or_404
from artifacts.models import Artifact

"""
Artifacts where the user bidded will  be stored into session when the user is logged in.
So a user can check his biddinds, but when they log out, this list will be lost.
"""

def my_bidding_list(request):
    """
    Ensures that the user's biddinds  are available when rendering every page

    """
    
    #It requests the existing biddings if there is one, or a blank dictionary if there's not.
    my_biddings = request.session.get('my_biddings', {})

    bidding_items = []
    total = 0
    product_count = 0
    
    for id in my_biddings.items():
        the_artifact = get_object_or_404(Artifact, pk=id)
        product_count += 1
        bidding_items.append({'id': id, 'artifact': the_artifact})
    
    return {'bidding_items': bidding_items, 'product_count': product_count}