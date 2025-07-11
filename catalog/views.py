from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponseForbidden, HttpResponse

from catalog.models import Product, Category
from .forms import ProductForm
from .models import Application

from django.core.cache import cache

from .services import products_by_category


def my_view(request):
    data = cache.get("my_key")
    if not data:
        data = "some expensive computation"
        cache.set("my_key", data, 60*15)
    return HttpResponse(data)

class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет необходимых прав снятия с публикации.")
        product.unpublish = True
        product.save()

        return redirect("catalog:info_product", pk=product_id)

class Home(ListView):
    model = Product

class ProdFromCat(ListView):
    model = Product
    template_name = "catalog/prod_from_category.html"
    def get_queryset(self):
        return products_by_category(self.kwargs['category_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем объект категории в контекст
        context['category'] = Category.objects.get(id=self.kwargs['category_id'])
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    model = Product
    template_name = "catalog/crud/create_product.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        """Кастомный метод для привязки пользователя к полю owner"""
        form.instance.owner = self.request.user  # 1. Привязываем пользователя
        return super().form_valid(form)  # 2. Сохраняем форму стандартным способом

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductForm
    model = Product
    template_name = "catalog/crud/update_product.html"
    success_url = reverse_lazy("catalog:home")

    def get_success_url(self):
        """ Перенаправление после редактирования на просмотр этой статьи """
        return reverse(
            "catalog:info_product", # Имя из path() в urls.py
            kwargs={"pk": self.object.pk}  # Параметры для подстановки
        )

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/crud/delete_product.html"
    success_url = reverse_lazy("catalog:home")

    def dispatch(self, request, *args, **kwargs):
        """Метод для прав доступа на удаление"""
        user = self.request.user
        if user.has_perm("catalog.can_delete_product"):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/crud/detail_product.html"

class Blank(LoginRequiredMixin, View):
    def get(self, request):
        """Получаем данные"""
        products = Product.objects.all()  # Получаем все продукты для выпадающего списка
        context_blank = {'products': products} # Передаем продукты в шаблон
        return render(request, "catalog/product_application.html", context_blank)

    def post(self, request):
        """Отправляем данные"""
        Application.objects.create(
            name=request.POST.get('name'),
            mail=request.POST.get('mail'),
            city=request.POST.get('city'),
            country=request.POST.get('country'),
            number=request.POST.get('number'),
            id_product_id=request.POST.get('id_product')  # Сохраняем ID продукта
        )
        return render(request, 'catalog/thank_you.html')

class AddProduct(View):
    def get(self, request):
        """Получаем данные"""
        categories = Category.objects.all()  # Получаем все категории
        context_add_product = {'categories': categories} # Передаем продукты в шаблон
        return render(request, "catalog/new_product.html", context_add_product)

    def post(self, request):
        """Отправляем данные"""
        Product.objects.create(
        name=request.POST.get('name'),
        breed=request.POST.get('breed'),
        description=request.POST.get('description'),
        img=request.FILES['img'],
        price=request.POST.get('price'),
        category_id=request.POST.get('category_id')  # Сохраняем ID продукта
        )
        return render(request, 'catalog/thank_you.html')
