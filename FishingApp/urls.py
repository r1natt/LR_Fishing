from django.conf.urls import url
from . import views


app_name = 'fishing'
urlpatterns = [
    url(r'^$', views.first_page, name='first_page'),
    url(r'^login$', views.index, name='index')
]
