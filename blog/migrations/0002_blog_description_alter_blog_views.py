from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите содержимое",
                null=True,
                verbose_name="Содержимое",
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="views",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Укажите количество просмотров",
                verbose_name="Количество просмотров",
            ),
        ),
    ]