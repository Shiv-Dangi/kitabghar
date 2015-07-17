from django.conf.urls import patterns, url
from django.conf import settings
from kitab import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^kitab/header/$', views.header, name='header'),
    url(r'^kitab/footer/$', views.footer, name='footer'),
    url(r'^kitab/sidebar/$', views.sidebar, name='sidebar'),
    url(r'^kitab/contact/$', views.contact, name='contact'),
    url(r'^kitab/aboutus/$', views.aboutus, name='aboutus'),
    url(r'^kitab/catagaries/$', views.catagaries, name='catagaries'),
    url(r'^kitab/howitworks/$', views.howitworks, name='howitworks'),
    url(r'^kitab/requestbook/$', views.requestbook, name='requestbook'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
