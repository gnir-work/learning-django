from django.conf.urls import include, url
from django.contrib import admin
from polls.urls import urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'pollsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'polls/', include(urlpatterns, namespace='polls')),
]
