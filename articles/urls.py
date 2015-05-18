from django.conf.urls import patterns, include, url
from articles.views import ArticleListView

urlpatterns = patterns('',
                       url(r'^$', ArticleListView.as_view(), name='article_list'),
)
