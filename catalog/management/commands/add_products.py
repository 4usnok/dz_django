from django.core.management.base import BaseCommand
from django.utils import timezone

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add products to the db"

    def handle(self, *args, **options):
        """Создание продуктов и категорий в админку"""
        # 1. Создаем основную категорию
        category, created = Category.objects.get_or_create(
            name="Собаки",  # -> Найденный или созданный объект (category)
            defaults={
                "description": "Домашние кошки различных пород"
            },  # -> Булево значение (created), указывающее, был ли объект создан (True) или найден (False)
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Создана категория: {category.name}"))
        else:
            self.stdout.write(
                self.style.WARNING(f"Категория {category.name} уже существует")
            )

        # 2. Создаем продукт
        product, created = Product.objects.get_or_create(
            name="Стаф",  # -> Найденный или созданный объект (product)
            defaults={
                "description": "Очень любвеобильный кот",
                "img": "",
                "category": category,
                "price": 1999,
                "created_at": timezone.now(),
                "updated_at": timezone.now(),
            },  # -> Булево значение (created), указывающее, был ли объект создан (True) или найден (False)
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Создан продукт: {product.name}"))
        else:
            self.stdout.write(
                self.style.WARNING(f"Продукт {product.name} уже существует")
            )
