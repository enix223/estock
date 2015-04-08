from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'estock.views.home', name='home'),
    # url(r'^estock/', include('estock.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^$', 'console.views_users.home', name='index'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),    
    
    url(r'^console/', include('console.urls')),
)
