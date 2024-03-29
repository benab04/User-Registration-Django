# Generated by Django 4.1.13 on 2024-03-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_submission_unique_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="todo",
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
                ("headline", models.CharField(max_length=255)),
                ("is_completed", models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name="Submission",
        ),
    ]
