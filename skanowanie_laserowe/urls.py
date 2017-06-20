from django.conf.urls import url
from skanowanie_laserowe import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]