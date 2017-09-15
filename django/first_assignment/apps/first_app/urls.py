from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^randomize$', views.randomize),
    url(r'^about_me$', views.about_me),
    url(r'^new_user$',views.new_user)
]
