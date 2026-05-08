from django.urls import path

from .views import (
    BlogCategoryListView,
    BlogPostDetailView,
    BlogPostListView,
    BlogTagListView,
)

urlpatterns = [
    path("categories/", BlogCategoryListView.as_view(), name="blog-category-list"),
    path("tags/", BlogTagListView.as_view(), name="blog-tag-list"),
    path("posts/", BlogPostListView.as_view(), name="blog-post-list"),
    path("posts/<slug:slug>/", BlogPostDetailView.as_view(), name="blog-post-detail"),
]
