# Generated by Django 4.2.6 on 2024-07-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
