from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^messageboard/$', views.messageboard),
    url(r'^messageboard/message/add_message$', views.new_message_process),
    url(r'^messageboard/message/(?P<message_id>\d+)/add_comment$', views.new_comment_process),
    url(r'^logout$', views.logout),
]
