# Generated by Django 4.1.1 on 2022-10-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_rename_rooms_room_alter_amenity_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="name",
            field=models.CharField(default="", max_length=180),
        ),
    ]
