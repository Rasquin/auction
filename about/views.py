from django.shortcuts import render

# Create your views here.
def about(request):
    """
    Get information about the site to the users
    """
    return render(request, "about.html")