from django.conf.urls import patterns, include, url
from django.contrib import admin
from financeweb.views import home, abc, home2, viewproject, updateproject, myprojects, newproject

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

)
