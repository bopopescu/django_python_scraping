from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^user/$', views.user, name='user'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^scraping_admin/$', views.scrapingAdmin, name='scraping_admin'),
    url(r'^admin999/$', views.admin, name='admin'),
    url(r'^fetchInterestingUrl/$', views.fetchInterestingUrl, name='fetchInterestingUrl'),
    url(r'^fetchNonInterestingUrl/$', views.fetchNonInterestingUrl, name='fetchNonInterestingUrl'),

]