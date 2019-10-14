from django.conf.urls import url
from .views import view_my_biddings, add_to_my_biddings

urlpatterns = [
    url(r'^$', view_my_biddings, name='view_my_biddings'),
    url(r'^add/(?P<id>\d+)', add_to_my_biddings, name='add_to_my_biddings'),
]