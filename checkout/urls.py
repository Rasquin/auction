from django.conf.urls import url
from .views import checkout

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', checkout, name='checkout'),
]