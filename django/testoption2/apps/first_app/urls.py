from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^tripdash$', views.tripdash),
    url(r'^logout$',views.logout),
    # url(r'^trippage$', views.trippage),
    # url(r'^createtrip$', views.trippage),
    # url(r'^addtrip$', views.addtrip),
    # url(r'^join$', views.join),
    # url(r'^details/(?P<id>\+d)$', views.details)
]
