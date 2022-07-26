from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import BookmarkViewSet, TagViewSet 

router = DefaultRouter()
router.register("bookmarks", BookmarkViewSet, basename="bookmarks")
router.register("tags", TagViewSet, basename="tags")

urlpatterns = [
    url('', include(router.urls))
]
 