# Generated by Django 4.2.6 on 2024-04-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrived', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo', models.CharField(blank=True, max_length=255, null=True)),
                ('update_date', models.CharField(blank=True, max_length=50, null=True)),
                ('parcel_collection', models.CharField(blank=True, max_length=50, null=True)),
                ('next_package', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
