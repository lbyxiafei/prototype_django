from django.urls import re_path 
from notes import views 
 
urlpatterns = [ 
    re_path(r'^api/bookmarks$', views.bookmarks),
]
