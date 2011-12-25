from django.conf.urls.defaults import patterns, include, url
from mysite.views import hello, index, current_date_time, hours_ahead

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
                       ('^$',index),
                       ('^hello/$',hello),
                       ('^time/$',current_date_time),
                       (r'^time/plus/(\d{1,2})$', hours_ahead),
)
