from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from blog.models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/crud/view_blog.html"
    context_object_name = "post"

class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blog/crud/create_post.html"
    fields = ("title", "content", "preview", "publication_sign", "number_of_views")
    success_url = reverse_lazy("blog:home")

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "content", "preview", "publication_sign", "number_of_views")
    template_name = "blog/crud/update_post.html"
    success_url = reverse_lazy("catalog:home")

class BlogDeleteView(DeleteView):
    model = BlogPost
    fields = ("title", "content", "preview", "publication_sign", "number_of_views")
    template_name = "blog/crud/delete_post.html"
    success_url = reverse_lazy("catalog:home")

