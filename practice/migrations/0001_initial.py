# Generated by Django 5.0.4 on 2024-07-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Passenger",
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
                ("firstName", models.CharField(max_length=50)),
                ("lastName", models.CharField(max_length=50)),
                ("travelPoints", models.IntegerField()),
            ],
        ),
    ]