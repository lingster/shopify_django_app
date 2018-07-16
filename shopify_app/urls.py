from django.conf.urls import url

import shopify_app.views

urlpatterns = [
    url(r'^$', shopify_app.views.login, name='shopify_app.views.login'),
    url(r'^authenticate/$', shopify_app.views.authenticate, name='shopify_app.views.authenticate'),
    url(r'^finalize/$', shopify_app.views.finalize, name='shopify_app.views.finalize'),
    url(r'^logout/$', shopify_app.views.logout, name='shopify_app.views.logout'),
]
