from django.urls import path
from .views import ListAllPostsView


urlpatterns = [
    path("all/", ListAllPostsView.as_view(), name="all-posts")
]