# Generated by Django 4.2.6 on 2024-04-01 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('name_of_purchase', models.CharField(max_length=255)),
                ('articul', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('telegram', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('purchase_image', models.ImageField(upload_to='purchase_image/')),
                ('payment_confirmation', models.ImageField(blank=True, null=True, upload_to='purchase_payment_confirmation')),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
