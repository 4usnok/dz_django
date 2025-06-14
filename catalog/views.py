from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db import models

from catalog.models import Product
from .models import Application  # Импортируем модель


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/product_list.html", context)

def contact(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/contacts.html", context)


def blank(request):
    products = Product.objects.all()  # Получаем все продукты для выпадающего списка
    context = {'products': products} # Передаем продукты в шаблон
    if request.method == "POST":
        # Создаем заявку
        Application.objects.create(
            name=request.POST.get('name'),
            mail=request.POST.get('mail'),
            city=request.POST.get('city'),
            country=request.POST.get('country'),
            number=request.POST.get('number'),
            id_product_id=request.POST.get('id_product')  # Сохраняем ID продукта
        )
        return HttpResponse("Спасибо за заявку!")
    return render(request, "catalog/product_application.html", context)

def add_product(request):
    products = Product.objects.all()  # Получаем все продукты для выпадающего списка
    context = {'products': products} # Передаем продукты в шаблон
    if request.method == "POST":
        # Создаем заявку
        Product.objects.create(
            name=request.POST.get('name'),
            breed=request.POST.get('breed'),
            description=request.POST.get('description'),
            img=request.POST.get('img'),
            price=request.POST.get('price'),
            category_id=request.POST.get('category_id')  # Сохраняем ID продукта
        )
        return HttpResponse("Новый питомец добавлен в каталог!")
    return render(request, "catalog/new_product.html", context)

