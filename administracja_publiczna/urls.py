from django.conf.urls import url
from administracja_publiczna import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^produkty/$', views.produkty, name='produkty'),
    url(r'^akty_prawne/$', views.akty_prawne, name='akty_prawne'),
    url(r'^partnerzy/$', views.partynerzy, name='partnerzy'),
    url(r'^produkty/adresat/$', views.adresat, name='adresat'),
    url(r'^produkty/turysta/$', views.turysta, name='turysta'),
    url(r'^produkty/ekolog/$', views.ekolog, name='ekolog'),
]
