from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from blog.models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/base_view.html"
    context_object_name = "posts"

    def get_queryset(self):
        """ Фильтрация опубликованных статей """
        queryset = super().get_queryset()
        return queryset.filter(publication_sign=True)

class InfoDetailView(LoginRequiredMixin, DetailView):
    login_url  = "/users/login/"
    model = BlogPost
    template_name = "blog/crud/post_detail.html"
    context_object_name = "info"

    def get_object(self, queryset=None):
        """ Увеличение счетчика просмотров при открытии отдельной статьи """
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object

class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blog/crud/create_post.html"
    fields = ("title", "content", "preview", "publication_sign", "number_of_views")
    success_url = reverse_lazy("blog:home")
    context_object_name = "new_post"


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/crud/update_post.html"
    fields = ("title", "content", "preview", "publication_sign", "number_of_views")

    def get_success_url(self):
        """ Перенаправление после редактирования на просмотр этой статьи """
        return reverse(
            "blog:info_post", # Имя из path() в urls.py
            kwargs={"pk": self.object.pk}  # Параметры для подстановки
        )

class BlogDeleteView(DeleteView):
    model = BlogPost
    fields = ("title", "content", "preview", "publication_sign", "number_of_views")
    template_name = "blog/crud/delete_post.html"
    success_url = reverse_lazy("blog:home")
    context_object_name = "posts"


