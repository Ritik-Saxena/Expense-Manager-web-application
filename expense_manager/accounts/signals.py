from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from expense.models import UserProfile

@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, display_name=instance.username, email=instance.email)

