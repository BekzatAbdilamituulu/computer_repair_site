# Generated by Django 5.0.4 on 2024-05-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Date'),
        ),
    ]