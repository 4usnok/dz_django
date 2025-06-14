from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product
from .forms import ApplicationForm
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
