# Generated by Django 4.2.6 on 2024-06-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0011_alter_warehouseproduct_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseproduct',
            name='status_many',
            field=models.BooleanField(default=False),
        ),
    ]
