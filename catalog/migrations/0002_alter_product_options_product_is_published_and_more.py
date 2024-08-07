# Generated by Django 5.0.7 on 2024-08-07 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name_product", "category"],
                "permissions": [
                    ("can_edit_product_description", "Can edit product description"),
                    ("can_edit_product_category", "Can edit product category"),
                    ("can_cancel_publication", "Can cancel publication of product"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(
                default=False,
                help_text="Опубликовать запись",
                verbose_name="Опубликовано",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="views_counter",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Укажите количество просмотров",
                verbose_name="Количество просмотров",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                help_text="Введите категорию",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="categories",
                to="catalog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(
                auto_now_add=True, null=True, verbose_name="Дата создания"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                auto_now_add=True,
                null=True,
                verbose_name="Дата последнего изменения записи",
            ),
        ),
        migrations.CreateModel(
            name="Version",
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
                    "version_number",
                    models.CharField(
                        blank=True,
                        help_text="Введите номер версии",
                        max_length=10,
                        null=True,
                        verbose_name="Номер версии",
                    ),
                ),
                (
                    "version_name",
                    models.CharField(
                        blank=True,
                        help_text="Введите название версии",
                        max_length=100,
                        null=True,
                        verbose_name="Название версии",
                    ),
                ),
                (
                    "is_version_active",
                    models.BooleanField(
                        default=False,
                        help_text="является ли версия активной",
                        verbose_name="Активная версия",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите продукт",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Version",
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
                "ordering": ["version_number", "version_name"],
            },
        ),
    ]