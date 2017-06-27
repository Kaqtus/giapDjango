from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^aktualnosci/$', views.aktualnosci, name='aktualnosci'),
    url(r'^aktualnosci/post/(?P<pk>[0-9]+)/$', views.single_post, name='single_post'),
    url(r'^sitemap/$', views.sitemap, name='sitemap'),
]
