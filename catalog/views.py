from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, FormView

from catalog.models import Product, Category
from .models import Application  # Импортируем модель


class Home(ListView):
    model = Product

class Contact(DetailView):
    model = Product
    template_name = "catalog/contacts.html"

class Blank(View):
    def get(self, request):
        """Получаем данные"""
        products = Product.objects.all()  # Получаем все продукты для выпадающего списка
        context = {'products': products} # Передаем продукты в шаблон
        return render(request, "catalog/product_application.html", context)

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
        context = {'categories': categories} # Передаем продукты в шаблон
        return render(request, "catalog/new_product.html", context)

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
