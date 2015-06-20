from django.conf.urls import patterns, url
from .views import About_meListView

urlpatterns = patterns('',
                       url(r'^$', About_meListView.as_view(), name='me'),
                       )