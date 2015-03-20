from django.conf.urls import patterns, include, url
from django.contrib import admin
from financeweb.views import home, abc, home2, login_user

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financeweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^homepage2$', home2, name='home2'),
	url(r'^signup$', abc, name='abc'),
	url(r'^signin', login_user, name='signin'),
)
