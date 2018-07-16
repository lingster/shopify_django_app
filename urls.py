from django.conf.urls import url, include

urlpatterns = [
    url(r'^login/', include('shopify_app.urls')),
    url(r'^', include('home.urls'), name='root_path'),
]
