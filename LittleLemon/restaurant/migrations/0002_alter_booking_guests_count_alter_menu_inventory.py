# Generated by Django 4.2 on 2023-05-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="guests_count",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="menu",
            name="inventory",
            field=models.IntegerField(),
        ),
    ]