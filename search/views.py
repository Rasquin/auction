from django.shortcuts import render
from decimal import Decimal
from artifacts.models import Artifact

# Create your views here.
def search_by_name(request):
    """
    Filters by name  the list of artifacts that are in the auction 
    """
    artifacts = Artifact.objects.filter(name__icontains=request.GET['q']) # for some reaseon dont want to get by artifact_name
    return render(request, "artifacts.html", {"artifacts": artifacts})

def filters(request):
    """
    Filters by price, age and origin the list of artifacts that are in the auction
    """
    the_artifacts = Artifact.objects.all()
    artifacts = []
    min_price =  Decimal(request.POST.get('min_price'))
    max_price =  Decimal(request.POST.get('max_price'))
    min_year =  Decimal(request.POST.get('min_year'))
    max_year =  Decimal(request.POST.get('max_year'))
    #request.form.get('recipe_name')
    artifact_origin = request.POST.get('artifact_origin')
    
    for artifact in the_artifacts:
        #if current_bidding_price is inside the limits of search
        if min_price <= artifact.current_bidding_price < max_price:
            #if the artifact.year is minor than the minimun year value possible
            if min_year == -2000 and artifact.year <= min_year:
                #if there is not imput for the origin filter
                if artifact_origin == '' :
                    artifacts.append(artifact)
                #if there is an imput for the origin filter
                else :
                    artifacts = Artifact.objects.filter(origin__search=artifact_origin) 
                    #Entry.objects.filter(body_text__search='cheese')
                
            #if  the artifact.year is inside the limits of search. It cannot be higher than max_year
            elif  min_year <= artifact.year <= max_year:
                #if there is not imput for the origin filter
                if artifact_origin == '' :
                    artifacts.append(artifact)
                #if there is an imput for the origin filter
                else :
                    artifacts = Artifact.objects.filter(origin__search='hola') 
                    #Entry.objects.filter(body_text__search='cheese')
                
        #if current_bidding_price >= max_price possible. It cannot be lower than min_price    
        elif max_price == 1000000 and artifact.current_bidding_price >= max_price:
            #if the artifact.year is minor than the minimun year value possible
            if min_year == -2000 and artifact.year <= min_year:
                #if there is not imput for the origin filter
                if artifact_origin == '' :
                    artifacts.append(artifact)
            #if  the artifact.year is inside the limits of search. It cannot be higher than max_year
            elif  min_year <= artifact.year <= max_year:
                artifacts.append(artifact)
                #if there is not imput for the origin filter
                if artifact_origin == '' :
                    artifacts.append(artifact)
            
    #artifacts = Artifact.objects.filter(name__icontains=request.GET['q'])
    return render(request, "artifacts.html", {"artifacts": artifacts})