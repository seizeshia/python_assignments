from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^adding$', views.adding),
    url(r'^results$', views.results)
]
