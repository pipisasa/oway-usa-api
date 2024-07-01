# Generated by Django 4.2.6 on 2024-06-30 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('my_warehouse', '0004_mywarehouse_city_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='mywarehouse',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
        ),
    ]