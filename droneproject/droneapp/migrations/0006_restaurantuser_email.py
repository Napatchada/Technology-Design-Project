# Generated by Django 5.0.4 on 2024-05-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("droneapp", "0005_remove_restaurantuser_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurantuser",
            name="email",
            field=models.EmailField(default="abc@gmail.com", max_length=254),
        ),
    ]
