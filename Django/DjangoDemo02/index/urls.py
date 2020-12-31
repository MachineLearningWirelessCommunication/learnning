from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^01-temp/$', views.temp),
]