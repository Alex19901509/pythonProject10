from django.db import models

from users.models import User


class Category(models.Model):
    name_category = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории ",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

        def __str__(self):
            return self.category_name


class Product(models.Model):
    name_product = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    picture = models.ImageField(
        upload_to="catalog/picture",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        blank=True,
        null=True,
        related_name="categories",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения записи",
    )
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Опубликовать запись",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        blank=True,
        null=True,
        related_name="products",
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name_product", "category"]
        permissions = [
            ('can_edit_product_description', 'Can edit product description'),
            ('can_edit_product_category', 'Can edit product category'),
            ('can_cancel_publication', 'Can cancel publication of product'),
        ]

        def __str__(self):
            return self.name_product


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='versions',
        on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Продукт",
        help_text="Выберите продукт",
    )
    version_number = models.CharField(
        max_length=10,
        verbose_name="Номер версии",
        help_text="Введите номер версии",
        null=True,
        blank=True,
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
        null=True,
        blank=True,
    )
    is_version_active = models.BooleanField(
        default=False,
        verbose_name="Активная версия",
        help_text="является ли версия активной",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number", "version_name"]

    def __str__(self):
        return self.version_name


