# Generated by Django 5.0.4 on 2024-06-08 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("service", "0007_servicecategory_name_ky_servicecategory_name_ru"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servicecategory",
            name="service",
        ),
        migrations.AddField(
            model_name="service",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="service.servicecategory",
            ),
        ),
    ]