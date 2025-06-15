from django.contrib import admin
from .forms import ApplicationForm

from catalog.models import Category, Product, Application



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "description")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "price", "name", "category")
    list_filter = ("category",)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    form = ApplicationForm  # Используем нашу форму
    list_display = ("id", "name", "city", "country")
    search_fields = ("name", "city", "country")
