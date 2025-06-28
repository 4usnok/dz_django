from blog.views import BlogCreateView, BlogListView, BlogUpdateView, BlogDeleteView, InfoDetailView
from django.urls import path


app_name = "blog"

urlpatterns = [
    path("home/", BlogListView.as_view(), name="home"),
    path("home/new/", BlogCreateView.as_view(), name="new_post"),
    path("home/<int:pk>/", InfoDetailView.as_view(), name="info_post"),
    path("home/update/<int:pk>/", BlogUpdateView.as_view(), name="update_post"),
    path("home/delete/<int:pk>", BlogDeleteView.as_view(), name="delete_post"),
]