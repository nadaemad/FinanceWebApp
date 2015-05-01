from django.conf.urls import patterns, include, url
from django.contrib import admin
from financeweb.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    ####this is for the new template####

    url(r'^$', home1, name='home1'),
    url(r'^home1$', home1, name='home1'),
    url(r'^signin1$', user_login1, name='user_login1'),
    url(r'^user_login1$', user_login1, name='user_login1'),
    url(r'^user_logout1$', user_logout1, name='user_logout1'),
    url(r'^index$', home1, name='home1'),
    url(r'^register1$', register1, name='register1'),
    url(r'^myaccount1/(?P<u_id>\d+)$', myaccount1, name='myaccount1'),
    url(r'^update_myaccount/(?P<u_id>\d+)$', update_myaccount, name='update_myaccount'),
    url(r'^allprojects1/(?P<u_id>\d+)$', allprojects1, name='allprojects1'),
    url(r'^newproject1/(?P<u_id>\d+)$', newproject1, name='newproject1'),
    url(r'^displayproject1/(?P<p_id>\d+)$', displayproject1, name='displayproject1'),
    url(r'^deleteproject1/(?P<p_id>\d+)/(?P<u_id>\d+)$', deleteproject1, name='deleteproject1'),

    url(r'^overview_project1/(?P<p_id>\d+)$', overview_project1, name='overview_project1'),
    url(r'^viewgrossprofit1/(?P<p_id>\d+)$', viewgrossprofit1, name='viewgrossprofit1'),
    url(r'^viewrevenues1/(?P<p_id>\d+)$', viewrevenues1, name='viewrevenues1'),
    url(r'^viewexpenses1/(?P<p_id>\d+)$', viewexpenses1, name='viewexpenses1'),


    url(r'^about1$', about1, name='about1'),
    url(r'^services1$', services1, name='services1'),
    url(r'^portfolio1$', portfolio1, name='portfolio1'),

    
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

