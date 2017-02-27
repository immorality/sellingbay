from django.conf.urls import url
from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload', views.update, name='update'),
    url(r'^logs', views.logs, name='logs'),
]