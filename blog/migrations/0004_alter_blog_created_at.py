from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blog_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="created_at",
            field=models.DateTimeField(
                blank=True,
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
    ]