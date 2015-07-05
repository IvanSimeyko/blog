from django.conf.urls import patterns, include, url
from django.contrib import admin
from articles.views import ArticleListView
import views

urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^article/', include('articles.urls', namespace="articles")),
    url(r'^contact/', include('contacts.urls', namespace="contacts")),
    url(r'^auth/', include('loginsys.urls', namespace="loginsys")),
    url(r'^foundation/', include('foundations.urls', namespace="foundation")),
    url(r'^about_me/', include('about_me.urls', namespace="about_me")),
    url(r'^category/(?P<pk>\d+)/$', views.category_eng, name='category_eng'),
    #url(r'^tag/(?P<id>\d+)/$', tag),
    )