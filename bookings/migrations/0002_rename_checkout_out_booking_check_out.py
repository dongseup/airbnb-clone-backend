# Generated by Django 4.1.1 on 2022-10-09 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="checkout_out",
            new_name="check_out",
        ),
    ]