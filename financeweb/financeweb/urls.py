from django.conf.urls import patterns, include, url
from django.contrib import admin
from financeweb.views import home, abc, home2, viewproject, updateproject, myprojects, newproject
from financeweb.views import home, abc, home2, login_user

from financeweb.views import home, home2, myaccount, signup, home3, editprofile

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financeweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', home, name='home'),
    url(r'^homepage2$', home2, name='home2'),
	url(r'^signup$', abc, name='abc'),
	url(r'^myprojects$', myprojects, name='myprojects'),
    url(r'^newproject$', newproject, name='newproject'),
    url(r'^viewproject/(?P<post_id>\d+)$', viewproject, name='viewproject'),
    url(r'^updateproject/(?P<post_id>\d+)$', updateproject, name='updateproject'),
    url(r'^viewproject/home$', home, name='home'),
    url(r'^viewproject/myprojects$', myprojects, name='myprojects'),
    url(r'^viewproject/viewproject/(?P<post_id>\d+)$', viewproject, name='viewproject'),


	url(r'^signin', login_user, name='signin'),
    url(r'^homepage$', home, name='home'),
    url(r'^homepage2$', home2, name='home2'),
    url(r'^homepage3/(?P<u_id>\d+)$', home3, name='home3'),
	url(r'^signup$', signup, name='signup'),
	url(r'^myaccount/(?P<u_id>\d+)$', myaccount, name='myaccount'),
	url(r'^editprofile/(?P<u_id>\d+)$', editprofile, name='editprofile'),

)
