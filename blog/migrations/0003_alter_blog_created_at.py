from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_description_alter_blog_views"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
    ]