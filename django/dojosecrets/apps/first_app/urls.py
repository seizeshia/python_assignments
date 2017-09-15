from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^wall$', views.wall),
    url(r'^post$', views.post),
    url(r'^logout$', views.logout),
    url(r'^posts/(?P<post_id>\d+)/likes$', views.likes)
    url(r'^posts/(?P<post_id>\d+)/destroy$',views.destroy')
]
