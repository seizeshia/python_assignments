from django.conf.urls import url
#CONTROLLER!
from . import views
urlpatterns = [
    url(r'^$', views.index)
]
