# Generated by Django 4.2.4 on 2023-09-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WikiInformation",
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
                ("topic", models.CharField(max_length=150)),
                ("article", models.TextField()),
            ],
        ),
    ]