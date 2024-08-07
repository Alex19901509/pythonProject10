# Generated by Django 5.0.7 on 2024-08-07 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_options_product_is_published_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите продукт",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="versions",
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
    ]