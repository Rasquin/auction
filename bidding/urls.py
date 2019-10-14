from django.conf.urls import url
from .views import place_bidding

urlpatterns = [
    url(r'^place_bidding/(?P<id>\d+)$', place_bidding, name='place_bidding'),
    
]