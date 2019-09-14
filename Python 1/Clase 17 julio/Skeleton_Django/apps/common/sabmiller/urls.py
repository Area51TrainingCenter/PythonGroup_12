# coding:utf-8
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

import views

urlpatterns = [
    url(
        r'^validate/?$',
        csrf_exempt(views.SABMillerUserValidation.as_view()),
        name='validate'
    ),
    url(
        r'^register/?$',
        csrf_exempt(views.SABMillerUserRegister.as_view()),
        name='register'
    ),
]
