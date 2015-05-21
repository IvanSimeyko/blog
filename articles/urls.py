from django.conf.urls import patterns, include, url
from articles.views import ArticleDetailView

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
                       )
