# Generated by Django 5.0.4 on 2024-06-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("service", "0008_remove_servicecategory_service_service_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                    "date",
                    models.DateTimeField(
                        auto_created=True, auto_now_add=True, verbose_name="Date"
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=12, verbose_name="Phone Number")),
                ("message", models.TextField(verbose_name="Message")),
            ],
        ),
    ]
