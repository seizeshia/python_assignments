from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^tripdash$', views.tripdash),
    url(r'^logout$',views.logout),
    url(r'^pageadd$', views.pageadd),
    url(r'^addingtrip$', views.addingtrip),
    url(r'^tripinfo/(?P<id>\d+)$',views.tripinfo),
    url(r'^join/(?P<id>\d+)$',views.join)
    # url(r'^join$', views.join),
    # url(r'^details/(?P<id>\+d)$', views.details)
]
