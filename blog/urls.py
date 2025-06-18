from blog.views import BlogCreateView, BlogListView, BlogUpdateView, BlogDeleteView
from django.urls import path


app_name = "blog"

urlpatterns = [
    path("home/", BlogListView.as_view(), name="home"),
    path("new_post/", BlogCreateView.as_view(), name="new_post"),
    path("update_post/", BlogUpdateView.as_view(), name="update_post"),
    path("delete_post/", BlogDeleteView.as_view(), name="delete_post"),
]