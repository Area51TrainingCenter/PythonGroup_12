# coding:utf-8
from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.UbigeoView.as_view(), name='ubigeo'),
]
