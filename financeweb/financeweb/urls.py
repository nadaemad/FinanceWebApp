from django.conf.urls import patterns, include, url
from django.contrib import admin
from sample.views import home, home2, myaccount, signup, home3, editprofile

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financeweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^homepage$', home, name='home'),
    url(r'^homepage2$', home2, name='home2'),
    url(r'^homepage3/(?P<u_id>\d+)$', home3, name='home3'),
	url(r'^signup$', signup, name='signup'),
	url(r'^myaccount/(?P<u_id>\d+)$', myaccount, name='myaccount'),
	url(r'^editprofile/(?P<u_id>\d+)$', editprofile, name='editprofile'),

)
