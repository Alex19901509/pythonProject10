# Generated by Django 5.0.6 on 2024-07-04 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_category",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=100,
                        verbose_name="Наименование категории",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории",
                        null=True,
                        verbose_name="Описание категории ",
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_product",
                    models.CharField(
                        help_text="Введите наименование продукта",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание продукта",
                        null=True,
                        verbose_name="Описание продукта",
                    ),
                ),
                (
                    "picture",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение товара",
                        null=True,
                        upload_to="catalog/picture",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(help_text="Введите цену", verbose_name="Цена"),
                ),
                (
                    "created_at",
                    models.DateField(
                        help_text="Введите дату создания записи",
                        verbose_name="Дата создания записи",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        help_text="Введите дату последнего изменения записи",
                        verbose_name="Дата последнего изменения записи",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
                "ordering": ["name_product", "price"],
            },
        ),
    ]
