# Generated by Django 4.2.6 on 2024-04-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_purchase_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='articul',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='color',
        ),
        migrations.AddField(
            model_name='purchase',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
