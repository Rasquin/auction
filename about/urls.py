from django.conf.urls import url, include
from .views import about

urlpatterns = [
    url(r'^$', about, name='about'),
]
