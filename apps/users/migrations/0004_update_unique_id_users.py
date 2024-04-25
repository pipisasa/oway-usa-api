from django.db import migrations


def migrate_unique_id(apps, schema_editor):
    User = apps.get_model('users', 'User')
    for user in User.objects.all():
        user.unique_id = generate_new_unique_id(user.id)
        user.save()


def migrate_unique_id_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_password'),
    ]

    operations = [
        migrations.RunPython(
            code=migrate_unique_id,
            reverse_code=migrate_unique_id_reverse,
        ),
    ]


def generate_new_unique_id(user_id):
    formatted_user_id = str(user_id).zfill(4)
    unique_id = f'OW{formatted_user_id}'
    return unique_id