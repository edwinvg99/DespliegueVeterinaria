# Generated by Django 4.2 on 2023-04-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("veterinaria", "0002_mascota"),
    ]

    operations = [
        migrations.AddField(
            model_name="mascota",
            name="edad",
            field=models.IntegerField(default=0, max_length=3),
        ),
    ]