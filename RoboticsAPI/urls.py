from django.conf.urls import patterns, include, url
#from Robotics import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RoboticsAPI.views.home', name='home'),
    # url(r'^RoboticsAPI/', include('RoboticsAPI.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', include('HomeAutomation.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
