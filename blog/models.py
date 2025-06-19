from django.db import models


class BlogPost(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
    )

    content = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )

    preview = models.ImageField(
        upload_to="product/img/",
        blank=True,
        null=True,
        verbose_name="Загрузите превью",
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Загрузите превью", )

    publication_sign = models.BooleanField(
        default=False,
    )

    number_of_views = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        default=0
    )

    class Meta:
        verbose_name = "Новый пост"
        verbose_name_plural = "Новые посты"
        ordering = [
            "title",
            "content",
            "preview",
            "creation_date",
            "number_of_views",
        ]

    def __str__(self):
        return self.content

class PostInfo(models.Model):
    title = models.ForeignKey(
        BlogPost,
        on_delete=models.SET_NULL,
        verbose_name="Заголовок",
        null=True,
        blank=True
    )

    content = models.TextField(
        verbose_name="Содержимое поста",
        help_text="Заполните описание поста",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="product/img/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите превью",
    )

    creation_date = models.DateTimeField(auto_now_add=True)

    publication_sign = models.BooleanField(
        default=False,
    )

    number_of_views = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )

    class Meta:
        verbose_name = "Информация о новом посте"
        verbose_name_plural = "Информация о новых постах"
        ordering = [
            "title",
            "content",
            "preview",
            "creation_date",
            "number_of_views",
        ]

    def __str__(self):
        return self.title
