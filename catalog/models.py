from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    breed = models.CharField(
        max_length=50,
        verbose_name="Наименование породы",
        help_text="Введите наименование породы",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    img = models.ImageField(
        upload_to="product/img/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(
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
            "name",
            "category",
            "price",
            "created_at",
            "updated_at",
        ]

    def __str__(self):
        return self.name
