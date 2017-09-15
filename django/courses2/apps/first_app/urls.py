from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.index),
    url(r'^adding$', views.adding),
    url(r'^removing/(?P<id>\d+)$', views.removing)
]
