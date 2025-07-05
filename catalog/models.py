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
        help_text="Введите наименование",
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
    date_now = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    unpublish = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "category",
            "price",
            "date_now",
            "updated_at",
            "unpublish",
        ]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите имя",
    )
    mail = models.CharField(
        max_length=50,
        verbose_name="Электронная почта",
        help_text="Введите электронную почту",
        blank=True,  # Необязательное в форме
        null=True  # Разрешить NULL в БД
    )

    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        help_text="Введите название города",
    )

    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        help_text="Введите название страны",
    )

    number =  models.CharField(
        max_length=20,
        verbose_name="Номер телефона",
        blank=True,
        null=True
    )

    id_product = models.ForeignKey(
        Product,  # Ссылка на модель Product
        on_delete=models.CASCADE,  # Удалять заявки при удалении продукта
        verbose_name="Товар",
        db_column='id_product'
    )


    class Meta:
        verbose_name = "Имя"
        verbose_name_plural = "Имена"


    def __str__(self):
        return self.name
