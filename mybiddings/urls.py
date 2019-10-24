from django.conf.urls import url
from .views import view_my_biddings

urlpatterns = [
    url(r'^$', view_my_biddings, name='view_my_biddings'),
]