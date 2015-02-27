"""
Definition of urls for SearchBubble.
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from django.contrib import admin
from app.forms import BootstrapAuthenticationForm

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^elements/all/$', 'app.views.all_elements', name='all_elements'),
    url(r'^category/all/$', 'app.views.all_categories', name='all_categories'), 
    url(r'^category/(?P<id>[-\w]+)/$', 'app.views.category', name='category_elements'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
