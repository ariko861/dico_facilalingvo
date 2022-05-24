from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.i18n import javascript_catalog

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('multidico',),
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'facilalingvo2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^i18n/', include('django.conf.urls.i18n')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^$', 'multidico.views.language_choice',name='language_choice'),
    url(r'^(?P<language>[-\w]+)/$','multidico.views.category_choice',name='category_choice'),
    url(r'^(?P<language>[-\w]+)/(?P<category>[-\w]+)/addword/','multidico.views.add_word',name='add_word'),
    url(r'^(change)/(\d{1,6})/$','multidico.views.change_word',name='change_word'),
    url(r'^(changeagain)/(\d{1,6})/$','multidico.views.change_word',name='change_word'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    (r'^accounts/', include('allauth.urls')),
    
)

