from django.conf.urls import url
from webpages import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]