from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

urlpatterns = []

urlpatterns += patterns('django_git.views',
    url(r'^(?P<repo>[\w_.-]+)/commit/(?P<commit>[\w\d]+)/blob/$', 'blob', name='django-git-blob'),
    url(r'^(?P<repo>[\w_.-]+)/commit/(?P<commit>[\w\d]+)/$', 'commit', name='django-git-commit'),
    url(r'^(?P<repo>[\w_.-]+)/$', 'repo', name='django-git-repo'),
    url(r'^$', 'index', name='django-git-index'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
