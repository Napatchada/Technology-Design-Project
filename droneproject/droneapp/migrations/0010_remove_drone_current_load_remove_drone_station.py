# Generated by Django 5.0.4 on 2024-05-16 22:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("droneapp", "0009_remove_drone_station_id_drone_station"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="drone",
            name="current_load",
        ),
        migrations.RemoveField(
            model_name="drone",
            name="station",
        ),
    ]