# Generated by Django 4.2.6 on 2024-05-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_remove_purchase_articul_remove_purchase_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='purchase_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='purchase_image/'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='telegram',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
