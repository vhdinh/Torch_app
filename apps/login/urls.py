from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^reggy/$', views.reggy, name="reggy"),
	url(r'^Welcome/$', views.logging, name="logging"),

]