from django.conf.urls import patterns, include, url
from django.contrib import admin
from financeweb.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financeweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', home, name='home'),


	url(r'^myprojects$', myprojects, name='myprojects'),
    url(r'^newproject$', newproject, name='newproject'),
    url(r'^viewproject/(?P<post_id>\d+)$', viewproject, name='viewproject'),
    url(r'^updateproject/(?P<post_id>\d+)$', updateproject, name='updateproject'),
    url(r'^viewproject/home$', home, name='home'),
    url(r'^viewproject/myprojects$', myprojects, name='myprojects'),
    url(r'^viewproject/viewproject/(?P<post_id>\d+)$', viewproject, name='viewproject'),


    url(r'^homepage2$', home2, name='home2'),
    url(r'^homepage3/(?P<u_id>\d+)$', home3, name='home3'),

	url(r'^myaccount/(?P<u_id>\d+)$', myaccount, name='myaccount'),
	url(r'^editprofile/(?P<u_id>\d+)$', editprofile, name='editprofile'),

    url(r'^register$', register, name='register'),
    url(r'^login$', user_login, name='login'), 
    url(r'^restricted', restricted, name='restricted'),
    url(r'^logout$', user_logout, name='logout'),

    url(r'^notauser$', notauser, name='notauser'),

)
