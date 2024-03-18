# Generated by Django 4.1.13 on 2024-03-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_submission"),
    ]

    operations = [
        migrations.CreateModel(
            name="user",
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
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name="todo",
        ),
    ]
