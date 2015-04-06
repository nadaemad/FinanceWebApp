from django.conf.urls import patterns, include, url
from django.contrib import admin
from financeweb.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financeweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', home, name='home'),


	url(r'^myprojects/(?P<u_id>\d+)$', myprojects, name='myprojects'),
    url(r'^myprojects/newproject/(?P<u_id>\d+)$', newproject, name='newproject'),
    url(r'^myprojects/viewproject/(?P<post_id>\d+)$', viewproject, name='viewproject'),
    url(r'^updateproject/(?P<post_id>\d+)$', updateproject, name='updateproject'),
    url(r'^viewproject/home$', home, name='home'),
    url(r'^viewproject/myprojects$', myprojects, name='myprojects'),
    url(r'^viewproject/viewproject/(?P<post_id>\d+)$', viewproject, name='viewproject'),

	url(r'^myaccount/(?P<u_id>\d+)$', myaccount, name='myaccount'),
	url(r'^myaccount/editprofile/(?P<u_id>\d+)$', editprofile, name='editprofile'),
    url(r'^myaccount/editprofile/myaccount/(?P<u_id>\d+)$', myaccount, name='myaccount'),

    url(r'^register$', register, name='register'),
    url(r'^login$', user_login, name='login'), 
    url(r'^restricted', restricted, name='restricted'),
    url(r'^logout$', user_logout, name='logout'),

    url(r'^notauser$', notauser, name='notauser'),

)
