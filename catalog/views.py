from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import View
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Category
from .forms import ProductForm
from .models import Application  # Импортируем модель


class Home(ListView):
    model = Product

class ProductCreateView(CreateView):
    form_class = ProductForm
    model = Product
    template_name = "catalog/crud/create_product.html"
    success_url = reverse_lazy("catalog:home")

class ProductUpdateView(UpdateView):
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

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/crud/delete_product.html"
    success_url = reverse_lazy("catalog:home")

class ProductDetailView(LoginRequiredMixin, DetailView):
    login_url  = "/users/login/"
    model = Product
    template_name = "catalog/crud/detail_product.html"

class Blank(View):
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
