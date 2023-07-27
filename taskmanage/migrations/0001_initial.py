# Generated by Django 4.2.3 on 2023-07-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tasksm",
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
                ("taskname", models.CharField(max_length=100)),
                ("taskpriority", models.CharField(max_length=3)),
                ("date", models.CharField(max_length=15)),
            ],
        ),
    ]