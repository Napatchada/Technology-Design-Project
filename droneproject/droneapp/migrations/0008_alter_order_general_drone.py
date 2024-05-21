# Generated by Django 5.0.4 on 2024-05-16 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("droneapp", "0007_order_general_city_order_general_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order_general",
            name="drone",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="droneapp.drone",
            ),
        ),
    ]
