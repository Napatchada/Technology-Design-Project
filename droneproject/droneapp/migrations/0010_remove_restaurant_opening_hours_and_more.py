# Generated by Django 5.0.4 on 2024-05-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("droneapp", "0009_delete_restaurantuser_restaurant_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="restaurant",
            name="opening_hours",
        ),
        migrations.RemoveField(
            model_name="restaurant",
            name="picture_link",
        ),
        migrations.AddField(
            model_name="restaurant",
            name="closing_time",
            field=models.TimeField(default="23:59:59"),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="icon",
            field=models.ImageField(blank=True, null=True, upload_to="img/"),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="opening_time",
            field=models.TimeField(default="00:00:00"),
        ),
    ]
