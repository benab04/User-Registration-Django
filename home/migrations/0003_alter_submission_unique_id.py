# Generated by Django 4.1.13 on 2024-03-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_rename_id_of_user_submission_unique_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="unique_id",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
