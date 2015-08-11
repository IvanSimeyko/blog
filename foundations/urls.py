from django.conf.urls import patterns, url
from foundations.views import foundation_results
from strip_foundation import strip_foundation

urlpatterns = [
    url(r'^results/$', foundation_results, name='foundation_results'),
    url(r'^strip/$', strip_foundation, name='strip_foundation'),
]
