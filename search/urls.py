from django.conf.urls import url
from .views import search_by_name, filters

urlpatterns = [
    url(r'^$', search_by_name, name='search_by_name'),
    url(r'^filters/$', filters, name='filters')
]