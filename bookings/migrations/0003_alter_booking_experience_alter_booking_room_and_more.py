# Generated by Django 4.1.1 on 2022-10-18 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_room_category"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("experiences", "0003_experience_category"),
        ("bookings", "0002_rename_checkout_out_booking_check_out"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="bookings",
                to="experiences.experience",
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="bookings",
                to="rooms.room",
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bookings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
