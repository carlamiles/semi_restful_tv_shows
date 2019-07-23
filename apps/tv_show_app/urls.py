from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^shows/new$', views.index),
    url(r'^add_show$', views.add_show),
    url(r'^shows/(?P<id>\d+)$', views.show_page),
    url(r'^shows/(?P<id>\d+)/edit$', views.show_edit_page),
    url(r'^edit_show/(?P<id>\d+)$', views.edit_show),
    url(r'^shows/(?P<id>\d+)/destroy$', views.delete_show),
    url(r'^shows$', views.all_shows),
]