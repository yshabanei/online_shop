# Generated by Django 5.0.7 on 2024-07-28 05:09

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0006_alter_brand_options_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="product",
            managers=[
                ("default_manager", django.db.models.manager.Manager()),
            ],
        ),
    ]
