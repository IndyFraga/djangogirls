from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^hola/$', views.hola, name='hola'),
	url(r'^fecha/$', views.fecha_actual, name='fecha_actual'),
	url(r'^fecha/mas/(\d{1,2})/$', views.horas_adelante, name='horas_adelante'),

]