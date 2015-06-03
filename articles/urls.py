from django.conf.urls import patterns, url
from articles.views import ArticleDetailView, add_like, add_comment

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
                       url(r'^addlike/(?P<pk>\d+)/$', add_like, name='add_like'),
                       url(r'^addcomment/(?P<pk>\d+)/$', add_comment, name='add_comment'),
                       )
