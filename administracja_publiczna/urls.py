from django.conf.urls import url
from administracja_publiczna import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^produkty/$', views.produkty, name='produkty'),
    url(r'^akty_prawne/$', views.akty_prawne, name='akty_prawne'),
    url(r'^aktualnosci/$', views.aktualnosci, name='aktualnosci'),
    url(r'^aktualnosci/post/(?P<pk>[0-9]+)/$', views.single_post, name='single_post'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^produkty/adresat/$', views.adresat, name='adresat'),
    url(r'^produkty/turysta/$', views.turysta, name='turysta'),
    url(r'^produkty/ekolog/$', views.ekolog, name='ekolog'),
]
