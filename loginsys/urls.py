from django.conf.urls import patterns, url
from loginsys.views import login, logout, register

urlpatterns = patterns('',
                       url(r'^login/$', login, name='log_in'),
                       url(r'^logout/$', logout, name='log_out'),
                       url(r'^register/$', register, name='register'),
                       )
