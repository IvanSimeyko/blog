from django.conf.urls import patterns, url
from foundations.views import foundation_results


urlpatterns = [
    url(r'^results/$', foundation_results, name='foundation_results'),
]
