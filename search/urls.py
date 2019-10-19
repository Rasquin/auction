from django.conf.urls import url
from .views import search_by_name

urlpatterns = [
    url(r'^$', search_by_name, name='search_by_name')
]