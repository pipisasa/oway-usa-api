# Generated by Django 4.2.6 on 2024-04-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_sites', '0002_catalogsite_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogsite',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
