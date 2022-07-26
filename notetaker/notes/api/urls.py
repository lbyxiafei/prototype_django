from django.urls import re_path 
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views 
from .views import BookmarkViewSet, TagViewSet 

router = DefaultRouter()
router.register("bookmark", BookmarkViewSet, basename="bookmark")
router.register("tag", TagViewSet, basename="tag")

urlpatterns = [
    url('', include(router.urls))
]
 