from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'PlayEnglish.views.home', name='home'),
    url(r'^game/', include('game.urls')),

)

urlpatterns +=\
    patterns(
        '',
        url(r'^login/$', 'django.contrib.auth.views.login',
            {'template_name': 'index.html'}, name='url_login'),

        url(r'^accounts/profile/$', 'PlayEnglish.views.home_barra',
            name='url_home_barra'),

        url(r'^logout/$', 'django.contrib.auth.views.logout',
            {'template_name': 'index.html'}, name='url_logout'),

        url(r'^accounts/login/$', 'django.contrib.auth.views.login',
            {'template_name': 'index.html'}, name='url_login'),

        url(r'^admin/', include(admin.site.urls)),
    )
