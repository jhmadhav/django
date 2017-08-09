from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'post^$', views.post_list, name='post_list'),
    url(r'^$', views.livetv, name='livetv'),
]