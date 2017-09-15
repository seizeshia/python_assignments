from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^$', views.results),
    url(r'^(?P<number>\d+)$', views.results)

]
