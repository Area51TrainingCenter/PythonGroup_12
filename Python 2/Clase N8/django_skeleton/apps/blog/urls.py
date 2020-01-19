from django.urls import path, include
from rest_framework import routers
from .views import CommentsViewset, PostSerializer

router = routers.DefaultRouter()
router.register(r'commets', CommentsViewset)
router.register(r'post', PostSerializer)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'),
         name='rest_framework')
]
