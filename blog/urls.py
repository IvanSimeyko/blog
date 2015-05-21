from django.conf.urls import patterns, include, url
from django.contrib import admin
from articles.views import ArticleListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ArticleListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/', include('articles.urls', namespace="articles")),
    url(r'^contact/', include('contacts.urls', namespace="contacts")),
)