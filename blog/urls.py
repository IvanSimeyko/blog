from django.conf.urls import patterns, include, url
from django.contrib import admin
from articles.views import ArticleListView

urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^article/', include('articles.urls', namespace="articles")),
    url(r'^contact/', include('contacts.urls', namespace="contacts")),
    url(r'^auth/', include('loginsys.urls', namespace="loginsys")),
    )