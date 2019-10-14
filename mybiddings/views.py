from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_my_biddings(request):
    """A View that renders the cart contents page"""
    return render(request, "mybiddings.html")
    
def add_to_my_biddings(request, id):
    """Add the artifact where I have bidded"""
    
    #cart = request.session.get('cart', {})
    my_biddings = request.session.get('my_biddings', {})
    
    my_biddings[id] = my_biddings.get(id) 


    request.session['my_biddings'] = my_biddings
    return redirect(reverse('index'))