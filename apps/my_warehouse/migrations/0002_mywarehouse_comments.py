# Generated by Django 4.2.6 on 2024-04-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mywarehouse',
            name='comments',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
