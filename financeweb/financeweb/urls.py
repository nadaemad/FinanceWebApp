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
    #url(r'^myprojects/viewproject/(?P<post_id>\d+)$', viewproject, name='viewproject'),
    url(r'^updateproject/(?P<post_id>\d+)$', updateproject, name='updateproject'),
    url(r'^viewproject/home$', home, name='home'),
    url(r'^viewproject/myprojects$', myprojects, name='myprojects'),
    #url(r'^viewproject/viewproject/(?P<post_id>\d+)$', viewproject, name='viewproject'),

	url(r'^myaccount/(?P<u_id>\d+)$', myaccount, name='myaccount'),
	url(r'^myaccount/editprofile/(?P<u_id>\d+)$', editprofile, name='editprofile'),
    url(r'^myaccount/editprofile/myaccount/(?P<u_id>\d+)$', myaccount, name='myaccount'),

    url(r'^register$', register, name='register'),
    url(r'^login$', user_login, name='login'), 
    url(r'^restricted', restricted, name='restricted'),
    url(r'^logout$', user_logout, name='logout'),

    url(r'^notauser$', notauser, name='notauser'),
    url(r'^myprojects/deleteproject/(?P<p_id>\d+)/(?P<u_id>\d+)$', deleteproject, name='deleteproject'),

    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^resetpassword/$', 'financeweb.views.reset', name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', 'financeweb.views.reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'financeweb.views.success', name='success'),
    url(r'^ourapp$', ourapp, name='ourapp'),
    url(r'^ourfeatures$', ourfeatures, name='ourfeatures'),
    url(r'^myprojects/home$', home, name='home'),

    url(r'^Allposts$', viewallposts, name="viewallposts"),
    url(r'^blog/viewpost/(?P<post_id>\d+)$', viewpost, name="viewpost"),
    url(r'^viewpost/viewpost/(?P<post_id>\d+)$', viewpost, name="viewpost"),
    url(r'^newpost$', makepost, name="makepost"),

    url(r'^viewproject/(?P<project_id>\d+)$', viewproject, name='viewproject'),
    url(r'^viewexpenses/(?P<project_id>\d+)$', viewexpenses, name="viewexpenses"),
    url(r'^viewrevenues/(?P<project_id>\d+)$', viewrevenues, name="viewrevenues"),
    url(r'^viewgrossprofit/(?P<project_id>\d+)$', viewgrossprofit, name="viewgrossprofit"),
    url(r'^overview_project/(?P<project_id>\d+)$', overview_project, name="overview_project"),
    url(r'^search_entries/(?P<u_id>\d+)$', search_entries, name='search_entries'),

    
)
