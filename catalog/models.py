from django.db import models


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
            return self.name_category


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
        verbose_name="Дата создания записи", help_text="Введите дату создания записи",blank=True,
        null=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения записи",
        help_text="Введите дату последнего изменения записи",blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name_product", "price"]

        def __str__(self):
            return self.name_product
