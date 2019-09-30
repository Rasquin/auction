from django.conf.urls import url, include
from .views import get_all_artifacts, bidding_status, get_one_artifact

urlpatterns = [
    url(r'^$', get_all_artifacts, name='artifacts'),
    url(r'^bidding/(?P<id>\d+)$', bidding_status, name='bidding_status'),
    url(r'^(?P<pk>\d+)/$', get_one_artifact, name='artifact'),
]