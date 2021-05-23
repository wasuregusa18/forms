# Generated by Django 3.1.1 on 2020-12-24 16:15

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comp_name", models.CharField(max_length=50)),
                ("email_address", models.EmailField(max_length=254)),
                ("street1", models.CharField(max_length=300)),
                ("street2", models.CharField(blank=True, max_length=300)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("post_code", models.CharField(max_length=15)),
                ("country", models.CharField(max_length=50)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("entry_date", models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "template",
                    models.FileField(blank=True, null=True, upload_to="temps/"),
                ),
                ("mapping", models.CharField(max_length=500)),
            ],
        ),
    ]