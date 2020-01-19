# coding:utf-8
from django.conf.urls import url
from .views import Home, Publication, ServiceCategory,\
    GenerateUsers, UsersListView, RedisView
from django.urls import path, include

urlpatterns = [
    path('apis/', include('blog.urls')),
    path('', Home.as_view()),
    path('category/', ServiceCategory.as_view()),
    path('publication/<int:id>/', Publication.as_view()),
    path('generate-users/', GenerateUsers.as_view()),
    path('redis/', RedisView.as_view()),

]
