from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^plans/', views.plans, name='plans'),
    url(r'^eula/', views.eula, name='eula'),
    url(r'^aup/', views.aup, name='aup'),
]
