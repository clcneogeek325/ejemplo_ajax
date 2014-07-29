from django.conf.urls import patterns, include, url

urlpatterns = patterns('alimentos.views',
    # Examples:
    url(r'^$', 'view_index', name='home'),
    url(r'^ws/alimentos/(?P<tipo>.*)/$', 'view_ws_alimento', name='web_service'),

)
