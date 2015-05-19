from django.conf.urls import patterns, url
from contacts.views import ContactCreateView

urlpatterns = patterns('',
                       url(r'^$', ContactCreateView.as_view(), name='create_contact'),
)
