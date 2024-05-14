# Generated by Django 5.0.4 on 2024-05-12 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChargingStations",
            fields=[
                ("station_id", models.AutoField(primary_key=True, serialize=False)),
                ("location", models.CharField(max_length=255)),
                ("capacity", models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name="Customers",
            fields=[
                ("customer_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("delivery_address", models.CharField(max_length=255)),
                ("phone", models.DecimalField(decimal_places=0, max_digits=10)),
                ("address", models.CharField(max_length=255)),
                ("state", models.CharField(max_length=255)),
                ("postcode", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Drone",
            fields=[
                ("drone_id", models.AutoField(primary_key=True, serialize=False)),
                ("station_id", models.IntegerField(blank=True, null=True)),
                ("battery_level", models.IntegerField(default=100)),
                (
                    "current_load",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Food",
            fields=[
                ("food_id", models.AutoField(primary_key=True, serialize=False)),
                ("food_name", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("total_weight", models.IntegerField()),
                ("category", models.CharField(max_length=255)),
                ("picture_link", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("payment_id", models.AutoField(primary_key=True, serialize=False)),
                ("customer_id", models.IntegerField()),
                ("card_name", models.CharField(max_length=255)),
                ("card_number", models.CharField(max_length=255)),
                ("cvc", models.IntegerField()),
                ("expiry_date", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Restaurants",
            fields=[
                ("restaurant_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("menu_items", models.CharField(max_length=255)),
                ("opening_hours", models.CharField(max_length=255)),
                ("picture_link", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ChargingStationStatus",
            fields=[
                (
                    "checking_station_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("status", models.BooleanField(default=True)),
                (
                    "station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="droneapp.chargingstations",
                    ),
                ),
                (
                    "drone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="droneapp.drone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FlightPaths",
            fields=[
                ("path_id", models.AutoField(primary_key=True, serialize=False)),
                ("start_location", models.CharField(max_length=255)),
                ("end_location", models.CharField(max_length=255)),
                ("battery_usage", models.IntegerField()),
                (
                    "drone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="droneapp.drone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("delivery_status", models.CharField(max_length=255)),
                ("order_placed", models.BooleanField(default=True)),
                ("order_packed", models.BooleanField(default=False)),
                ("order_shipped", models.BooleanField(default=False)),
                ("service_fee", models.IntegerField(default=5)),
                ("delivery_fee", models.IntegerField(default=5)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="droneapp.customers",
                    ),
                ),
                (
                    "drone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="droneapp.drone",
                    ),
                ),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="droneapp.food",
                    ),
                ),
                (
                    "payment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="droneapp.payment",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="food",
            name="restaurant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="droneapp.restaurants",
            ),
        ),
    ]