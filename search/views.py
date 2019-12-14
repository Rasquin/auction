from django.shortcuts import render
from decimal import Decimal
from artifacts.models import Artifact
#import numpy

# Create your views here.
def search_by_name(request):
    """
    Filters by name  the list of artifacts that are in the auction 
    """
    artifacts = Artifact.objects.filter(name__icontains=request.GET['artifact_name']) # for some reason doesnt want to get by artifact_name
    return render(request, "artifacts.html", {"artifacts": artifacts})

def filters(request):
    """
    Filters by price, age and origin the list of artifacts that are in the auction
    """
    the_artifacts = Artifact.objects.all()
    artifacts = []
    min_price =  Decimal(request.GET.get('min_price'))
    max_price =  Decimal(request.GET.get('max_price'))
    min_year =  int(request.GET.get('min_year'))
    max_year =  int(request.GET.get('max_year'))
    
    artifact_origin = request.GET.get('artifact_origin')
    print(artifact_origin)
    
    for artifact in the_artifacts:
        # filter the price
        if min_price <= artifact.current_bidding_price < max_price:
            #filter the year/age
            if artifact.year in range(min_year, max_year):
                #filter the origin
                if artifact_origin == '':
                    artifacts.append(artifact)
                else:
                    artifacts = Artifact.objects.filter(origin__icontains=artifact_origin)

    return render(request, "artifacts.html", {"artifacts": artifacts})
    
    
    