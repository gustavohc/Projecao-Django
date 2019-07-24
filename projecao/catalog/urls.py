from django.conf.urls import url
from catalog import views

# TEMPLATE TAGGING
app_name = 'catalog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addhouse/$', views.AddHouseForm, name='add_house')
]