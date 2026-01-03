from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    # Create profile safely (avoid duplicates)
    profile, _ = UserProfile.objects.get_or_create(
        user=instance,
        defaults={
            "user_firstname": instance.first_name or "",
            "user_last_name": instance.last_name or "",
            "user_preferred_name": instance.username or "",
            "tier": UserProfile.TIER_FREE,
            # ✅ default account type (you can change default later)
            "account_type": UserProfile.TYPE_TRADESPERSON,
        }
    )
