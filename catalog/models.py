from django.db import models


class Category(models.Model):
    name_category = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    info_category = models.CharField(
        max_length=200,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name_category"]

    def __str__(self):
        return self.name_category

class Product(models.Model):
    name_product = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    info_product = models.CharField(
        max_length=200,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    img_product = models.ImageField(
        upload_to="product/img",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category_product = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        null=True,
        blank=True,
        related_name="products"
    )
    purchase_price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Укажите цену за покупку"
    )
    created_at = models.DateField(
        verbose_name="Дата создания", help_text="Укажите дату создания"
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name_product",
            "category_product",
            "purchase_price",
            "created_at",
            "updated_at",
        ]

    def __str__(self):
        return self.name_product
