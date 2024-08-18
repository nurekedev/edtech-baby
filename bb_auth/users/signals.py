from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import bProfile, bUser

@receiver(post_save, sender=bUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        bProfile.objects.create(user=instance)
