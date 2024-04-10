from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User
from apps.users.models.users.users import generate_unique_id


@receiver(post_save, sender=User)
def set_unique_id(sender, instance, created, **kwargs):

    if created or not instance.unique_id:
        instance.unique_id = generate_unique_id(instance.id)
        instance.save()