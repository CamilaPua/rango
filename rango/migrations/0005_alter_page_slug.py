# Generated by Django 4.0.2 on 2023-09-21 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_page_slug_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(),
        ),
    ]
