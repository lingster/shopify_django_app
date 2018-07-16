from django.conf.urls import url

import home.views

urlpatterns = [
    url(r'^$', home.views.index, name='home.views.index'),  # was root_path
    url(r'^design/$', home.views.design, name='home.views.design'),
    url(r'^welcome/$', home.views.welcome, name='home.views.welcome'),
]
