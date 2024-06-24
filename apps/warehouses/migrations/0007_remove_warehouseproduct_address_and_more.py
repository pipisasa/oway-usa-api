# Generated by Django 4.2.6 on 2024-06-06 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('countries', '0001_initial'),
        ('warehouses', '0006_rename_warehouse_warehouseproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='address',
        ),
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='country',
        ),
        migrations.AddField(
            model_name='warehouseproduct',
            name='country_of_destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destination_warehouseproducts', to='countries.country'),
        ),
        migrations.AddField(
            model_name='warehouseproduct',
            name='country_of_origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origin_warehouseproducts', to='countries.country'),
        ),
        migrations.AddField(
            model_name='warehouseproduct',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='warehouseproduct',
            name='length',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='warehouseproduct',
            name='width',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='warehouseproduct',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities.city')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='countries.country')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='warehouseproduct',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='warehouses.warehouse'),
        ),
    ]