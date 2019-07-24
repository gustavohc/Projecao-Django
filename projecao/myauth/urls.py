from django.conf.urls import url
from . import views

# TEMPLATE URLS
app_name = 'myauth'

urlpatterns = [
    url(r'^register/$', views.register, name='register'), 
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
]